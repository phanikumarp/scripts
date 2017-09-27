#!/bin/bash
    #
    # Opsmx-watchdog
    #
    # Run as a cron job to keep an eye on what_to_monitor which should always
    # be running. Restart what_to_monitor and send notification as needed.
    #
    # This needs to be run as root or a user that can start system services.
    # Authour : Phani
    # Revisions: 1.0

    ###  Services Names ###
        TOMCAT_NAME=tomcat
        POSTGRES_NAME=postgres
        CASSERVICE_NAME=opsmx-cas-services.jar
        STACKDRIVER_NAME=Stackdriver.jar
        LOGSTASH_NAME=logstash
        HBASE_NAME=hbase
        REDIS_NAME=redis
        TSDB_NAME=opentsdb
        APACHE_NAME=apache
        STORM_NAME=storm



    ## Services to start  ###
        TOMCAT_START='sudo /root/apache-tomcat-7.0.75/bin/startup.sh'
        POSTGRES_START='sudo /etc/init.d/postgresql start'
        CASSERVICE_JAR_START='sudo -u ubuntu java -Dserver.port=8090  -jar /home/ubuntu/opsmx-cas-services.jar > /home/ubuntu/cas_service.log'
        STACKDRIVER_JAR_START='sudo -u ubuntu java -Dserver.port=9090  -jar /home/ubuntu/Stackdriver.jar > /home/ubuntu/datadog_service.log'
        LOGSTASH_START='sudo service logstash start'
        HBASE_START='sudo /root/hbase-1.2.5/bin/start-hbase.sh'
        REDIS_START='sudo /etc/init.d/redis-server start'
        TSDB_START='sudo /etc/init.d/opentsdb start'
        APACHE_START='sudo /etc/init.d/apache2 start'
        STORM_START='storm jar /home/ubuntu/Storm-Event-Processing.jar com.opsmx.eventprocessing.EventProcessingTopology'

		NOTICE='/tmp/opswatchdog.txt'
		NOTIFY=phani@opsmx.com
		GREP=/bin/grep
		PS=/bin/ps
		NOP=/bin/true
		DATE=/bin/date
		# MAIL=/bin/mail
		RM=/bin/rm

    while true;
    do
     # OM01
      $PS -ef|$GREP -v grep|$GREP $TOMCAT_NAME >/dev/null 2>&1
      case "$?" in
       0)
       # It is running in this case so we do nothing.
        echo "$TOMCAT_NAME is RUNNING OK. Relax."

       $NOP
       ;;
       1)
       echo "$TOMCAT_NAME is NOT RUNNING. Starting $TOMCAT_NAME and sending notices."
       $TOMCAT_START 2>&1 >/dev/null &
       echo "$TOMCAT_NAME was not running and was started on `$DATE`" > $NOTICE
       # $MAIL -n -s "watchdog notice" -c $NOTIFY < $NOTICE
       #$RM -f $NOTICE
       ;;
      esac

      # OM02
      $PS -ef|$GREP -v grep|$GREP $POSTGRES_NAME >/dev/null 2>&1
      case "$?" in
       0)
       # It is running in this case so we do nothing.
        echo "$POSTGRES_NAME is RUNNING OK. Relax."

       $NOP
       ;;
       1)
       echo "$POSTGRES_NAME is NOT RUNNING. Starting $POSTGRES_NAME and sending notices."
       $POSTGRES_START 2>&1 >/dev/null &
       echo "$POSTGRES_NAME was not running and was started on `$DATE`" > $NOTICE
       # $MAIL -n -s "watchdog notice" -c $NOTIFY < $NOTICE
       #$RM -f $NOTICE
       ;;
      esac

      $PS -ef|$GREP -v grep|$GREP $CASSERVICE_NAME >/dev/null 2>&1
      case "$?" in
       0)
       # It is running in this case so we do nothing.
        echo "$CASSERVICE_NAME is RUNNING OK. Relax."

       $NOP
       ;;
       1)
       echo "$CASSERVICE_NAME is NOT RUNNING. Starting $CASSERVICE_NAME and sending notices."
       $CASSERVICE_JAR_START >/home/ubuntu/cas_service.log &
       echo "$CASSERVICE_NAME was not running and was started on `$DATE`" > $NOTICE
       # $MAIL -n -s "watchdog notice" -c $NOTIFY < $NOTICE
       #$RM -f $NOTICE
       ;;
      esac

      $PS -ef|$GREP -v grep|$GREP $STACKDRIVER_NAME >/dev/null 2>&1
      case "$?" in
       0)
       # It is running in this case so we do nothing.
        echo "$STACKDRIVER_NAME is RUNNING OK. Relax."

       $NOP
       ;;
       1)
       echo "$STACKDRIVER_NAME is NOT RUNNING. Starting $STACKDRIVER_NAME and sending notices."
       $STACKDRIVER_JAR_START >/home/ubuntu/datadog_service.log &
       echo "$STACKDRIVER_NAME was not running and was started on `$DATE`" > $NOTICE
       # $MAIL -n -s "watchdog notice" -c $NOTIFY < $NOTICE
       #$RM -f $NOTICE
       ;;
      esac

      $PS -ef|$GREP -v grep|$GREP $LOGSTASH_NAME >/dev/null 2>&1
      case "$?" in
       0)
       # It is running in this case so we do nothing.
        echo "$LOGSTASH_NAME is RUNNING OK. Relax."

       $NOP
       ;;
       1)
       echo "$LOGSTASH_NAME is NOT RUNNING. Starting $LOGSTASH_NAME and sending notices."
       $LOGSTASH_START  2>&1 >/dev/null &
       echo "$LOGSTASH_NAME was not running and was started on `$DATE`" > $NOTICE
       # $MAIL -n -s "watchdog notice" -c $NOTIFY < $NOTICE
       #$RM -f $NOTICE
       ;;
      esac

          $PS -ef|$GREP -v grep|$GREP $HBASE_NAME >/dev/null 2>&1
      case "$?" in
       0)
       # It is running in this case so we do nothing.
        echo "$HBASE_NAME is RUNNING OK. Relax."

       $NOP
       ;;
       1)
       echo "$HBASE_NAME is NOT RUNNING. Starting $HBASE_NAME and sending notices."
       $HBASE_START 2>&1 >/dev/null &
       echo "$HBASE_NAME was not running and was started on `$DATE`" > $NOTICE
       # $MAIL -n -s "watchdog notice" -c $NOTIFY < $NOTICE
       #$RM -f $NOTICE
       ;;
      esac

          $PS -ef|$GREP -v grep|$GREP $REDIS_NAME >/dev/null 2>&1
      case "$?" in
       0)
       # It is running in this case so we do nothing.
        echo "$REDIS_NAME is RUNNING OK. Relax."

       $NOP
       ;;
       1)
       echo "$REDIS_NAME is NOT RUNNING. Starting $REDIS_NAME and sending notices."
       $REDIS_START 2>&1 >/dev/null &
       echo "$REDIS_NAME was not running and was started on `$DATE`" > $NOTICE
       # $MAIL -n -s "watchdog notice" -c $NOTIFY < $NOTICE
       #$RM -f $NOTICE
       ;;
      esac

          $PS -ef|$GREP -v grep|$GREP $TSDB_NAME >/dev/null 2>&1
      case "$?" in
       0)
       # It is running in this case so we do nothing.
        echo "$TSDB_NAME is RUNNING OK. Relax."

       $NOP
       ;;
       1)
       echo "$TSDB_NAME is NOT RUNNING. Starting $TSDB_NAME and sending notices."
       $TSDB_START 2>&1 >/dev/null &
       echo "$TSDB_NAME was not running and was started on `$DATE`" > $NOTICE
       # $MAIL -n -s "watchdog notice" -c $NOTIFY < $NOTICE
       #$RM -f $NOTICE
       ;;
      esac

          $PS -ef|$GREP -v grep|$GREP $APACHE_NAME >/dev/null 2>&1
      case "$?" in
       0)
       # It is running in this case so we do nothing.
        echo "$APACHE_NAME is RUNNING OK. Relax."

       $NOP
       ;;
       1)
       echo "$APACHE_NAME is NOT RUNNING. Starting $APACHE_NAME and sending notices."
       $APACHE_START 2>&1 >/dev/null &
       echo "$APACHE_NAME was not running and was started on `$DATE`" > $NOTICE
       # $MAIL -n -s "watchdog notice" -c $NOTIFY < $NOTICE
       #$RM -f $NOTICE
       ;;
      esac

      $PS -ef|$GREP -v grep|$GREP $STORM_NAME >/dev/null 2>&1
      case "$?" in
       0)
       # It is running in this case so we do nothing.
        echo "$STORM_NAME is RUNNING OK. Relax."

       $NOP
       ;;
       1)
       echo "$STORM_NAME is NOT RUNNING. Starting $STORM_NAME and sending notices."
       $STORM_START 2>&1 >/home/ubuntu/Storm.log &
       echo "$STORM_NAME was not running and was started on `$DATE`" > $NOTICE
       # $MAIL -n -s "watchdog notice" -c $NOTIFY < $NOTICE
       #$RM -f $NOTICE
       ;;
      esac

      sleep 1m
      #exit
    done
