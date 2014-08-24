#!/bin/sh

portNumber=$1
ifFile=$2

echo 'Parameter PortNumber'
echo $portNumber
echo 'Parameter ifFile'
echo $ifFile

ifDir=$(dirname "$2")

ifBase=$(basename "$2")

echo "IF BAse" $ifBase

if [ "$3" = "" ]
then
  exeFile=`basename $ifFile .if`.x
else
  exeFile=`basename $ifFile .if`.$3
fi

cd $ifDir

exeOutputFile=ifExeOutput.$$.txt
stateFile=ifStates.$$.state
transitionFile=ifTransitions.$$.aut

#exeOutputFile=$ifDir/ifExeOutput.$$.txt
#stateFile=$ifDir/ifStates.$$.state
#transitionFile=$ifDir/ifTransitions.$$.aut

#cd $ifDir

echo 'PWD' $PWD

echo 'Compiling...'


$IF/com/if2gen $ifBase

if [ $? -eq 1 ]
then
  echo '-EOF-'
#  rm -f $ifDir/`basename $ifFile .if`.* $stateFile $transitionFile
   rm -f $stateFile $transitionFile
else
  echo 'Running...'
  ./$exeFile -q $stateFile -t $transitionFile -me -ms -discard 2>&1 | tee $exeOutputFile

  grep -q "error state" $exeOutputFile 

  if [ $? -eq 0 ]
  then
    echo 'Analysing results...'
    ## (NB: the next line is required to inform RTDS that the output for the check is over. If
    ##  it isn't there, RTDS GUI will remain unresponsive until the checker GUI is closed)
    echo '-EOF-'
    #python "$RTDS_HOME/share/3rdparty/IFx/if2msc.py" -AU $exeOutputFile $transitionFile $stateFile $ifFile $portNumber
    python "$RTDS_HOME/share/3rdparty/IFx/if2msc.py" -AU $exeOutputFile $transitionFile $stateFile $ifBase $portNumber
  else
    echo "no error state"
    echo '-EOF-'
    rm -f $exeOutputFile $stateFile $transitionFile *.C *.h *.x *.m4 *.o
    
  fi
#rm -f $ifDir/`basename $ifFile .if`.* $exeOutputFile $stateFile $transitionFile

#--Modified by JP
rm -f *.C *.h *.x *.m4 *.o
fi
