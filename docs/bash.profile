#ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl
#chmod u+x ~/scripts/judge.sh
#ls -l ~/scripts/judge.sh

#java
export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
export GRADLE_HOME=/Users/aregsarkissian/Development/gradle-2.0
export M2_HOME=/usr/local/Cellar/maven/3.2.3/libexec
export M2=$M2_HOME/bin

#python
export PYTHON_HOME=/usr/local/bin/python
export PYTHON3_HOME=$(which python3)

#postgres
export POSTGRES_HOME=/Applications/Postgres.app/Contents/Versions/9.3
export PGDATA=/usr/local/var/postgres/data

#path
export PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
export PATH=$JAVA_HOME/bin:$GRADLE_HOME/bin:$POSTGRES_HOME/bin:$PATH
#export PATH="$PATH:$HOME/.rvm/bin"
export PATH=$PATH:~/scripts
export PATH=$M2:$PATH

alias pgstart='pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start'
alias pgstop='pg_ctl -D /usr/local/var/postgres stop -s -m fast'
alias pipfreeze='pip freeze > requirements.txt'
alias pipinstall='pip install -r requirements.txt'
