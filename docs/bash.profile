#ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl
#chmod u+x ~/scripts/judge
#ls -l ~/scripts/judge.sh
JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
POSTGRES_HOME=/Applications/Postgres.app/Contents/Versions/9.3
GRADLE_HOME=/Users/aregsarkissian/Development/gradle-2.0
PYTHON_HOME=/usr/local/bin/python
PYTHON3_HOME=$(which python3)
PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
export PGDATA=/usr/local/var/postgres/data
export FLASK_DEBUG=True
export PATH=$JAVA_HOME/bin:$GRADLE_HOME/bin:$POSTGRES_HOME/bin:$PATH
export PATH="$PATH:$HOME/.rvm/bin" # Add RVM to PATH for scripting
export PATH=$PATH:~/scripts
alias pgstart='pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start'
alias pgstop='pg_ctl -D /usr/local/var/postgres stop -s -m fast'
alias pipfreeze='pip freeze > requirements.txt'
alias pipinstall='pip install -r requirements.txt'
