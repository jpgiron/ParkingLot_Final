#!/bin/sh

portNumber=$1
ifFile=$2

ifDir=`dirname $2`
#ifBase=`basename $2`
#if [ "$3" = "" ]
#then
#  exeFile=`basename $ifFile .if`.x
#else
#  exeFile=`basename $ifFile .if`.$3
#fi

exeOutputFile=$ifDir/ifExeOutput.*.txt
stateFile=$ifDir/ifStates.*.state
transitionFile=$ifDir/ifTransitions.*.aut

#cd $ifDir

#echo 'Compiling...'
#$IF/com/if2gen $ifBase

#if [ $? -eq 1 ]
#then
#  echo '-EOF-'
#  rm -f $ifDir/`basename $ifFile .if`.* $stateFile $transitionFile
#else
#  echo 'Running...'
#  ./$exeFile -q $stateFile -t $transitionFile -me -ms -discard 2>&1 | tee $exeOutputFile#

#  grep -q "error state" $exeOutputFile 

#  if [ $? -eq 0 ]
#  then
#    echo 'Analysing results...'
    ## (NB: the next line is required to inform RTDS that the output for the check is over. If
    ##  it isn't there, RTDS GUI will remain unresponsive until the checker GUI is closed)
#    echo '-EOF-'
    python "$RTDS_HOME/share/3rdparty/IFx/if2msc.py" -AU $exeOutputFile $transitionFile $stateFile $ifFile   $portNumber
#  else
#    echo "no error state"
#    echo '-EOF-'
#  fi
#rm -f $ifDir/`basename $ifFile .if`.* $exeOutputFile $stateFile $transitionFile
#fi
