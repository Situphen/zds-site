#!/bin/bash


function _in {
  # credits: https://stackoverflow.com/a/8574392
  local e match="$1"
  shift
  for e; do [[ "$e" == "$match" ]] && return 0; done
  return 1
}


## CI folding

ZDS_SHOW_CI_FOLD=0
if _in "--ci-output" "$@"; then
    ZDS_SHOW_CI_FOLD=1
fi


function zds_fold_category {
    # No-op to remove this command. Will be truly removed when all side-effects are ok.
    true;
}


zds_fold_current=""
function zds_fold_start {
    if [[ $ZDS_SHOW_CI_FOLD == 1 ]]; then
        if [[ $zds_fold_current == $1 ]]; then # for virtualenv fold
            return
        fi

        zds_fold_current="$1"
        echo "::group::${zds_fold_current}"
    fi

    print_info "$2" --bold
}


function zds_fold_end {
    if [[ $ZDS_SHOW_CI_FOLD == 1 ]] && [[ $zds_fold_current =~ "" ]]; then
        zds_travis_fold "::endgroup::"
        zds_fold_current=""
    fi
}
## end


## start zmd start & stop function
function zds_start_zmd {
    npm run server --prefix zmd/node_modules/zmarkdown -- --silent; exVal=$?

    if [[ $exVal != 0 ]]; then
        zds_fold_end
        gateway "!! Cannot start zmd" $exVal
        exit 1
    fi
}


function zds_stop_zmd {
    node ./zmd/node_modules/pm2/bin/pm2 kill; exVal=$?

    if [[ $exVal != 0 ]]; then
        print_error "Warning: Cannot stop zmd"
    fi
}
## end


function gateway {
    if [[ $2 != 0 ]]; then
        print_error "$1"
        exit $2
    fi
}


## start print function
function print_info {
    if [[ "$2" == "--bold" ]]; then
        echo -en "\033[36;1m"
    else
        echo -en "\033[0;36m"
    fi
    echo "$1"
    echo -en "\033[00m"
}


function print_error {
    echo -en "\033[31;1m"
    echo "$1"
    echo -en "\033[00m"
}
## end
