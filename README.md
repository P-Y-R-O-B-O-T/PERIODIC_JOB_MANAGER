# PERIODIC_JOB_MANAGER

![](ZZZ/ZZZ.jpg)

* Do you often forget about your health when you are working on something ?

* Do you often feel dehydrated ?

* Do you want to run a GUI application at some specific interval or at specific time ?

* Do you want some special custom notification ?

* Do you want to run a script at some interval or at some specific time ?

## ISSUES WITH CRON JOBS AND OTHER SYSTEMD UNITS
* `Cron jobs` and `systemd units` can't send notification, even if they send it is either security issue or it is very complex to setup

* Both of them either cant't launch graphical appliation easily

## COMPATIBILITY
* This is tested on `ubuntu 22`, `xorg` and `bash` as of now

* Onen to solve issues and contribute

# INSTALLATION
> Run the following commands:

* `git clone https://github.com/P-Y-R-O-B-O-T/PERIODIC_JOB_MANAGER.git`

* `cd PERIODIC_JOB_MANAGER`

* `chmod +x install.sh`

# CONFIGURATION
* A base configuration file is given with some notification things

* For example, this is a single job in the config file

```json
{
	"HAVE SOME SAXX": {"TYPE": "LONG",
					   "INTERVAL": 20,
					   "MIN_TIME_TO_START": 0,
					   "TIME": [[19, 8]],
					   "COMMAND": "notify-send 'Surprize motherfuckers' 'Have Some SAXX' --urgency=critical --expire-time=1000 --app-name=PDF --icon=/home/$USER/Downloads/sexy.png"},
}
```

* `TYPE`: if your job is a long runnging job > `30 s` then it it should be `LONG` else `ONESHOT` is fine

* `INTERVAL`: the value of interval after which the jobs repeats itself, this value is in seconds

* `MIN_TIME_TO_START`: the time in seconds after booting of the computer the command/script should be run first

* `TIME`: a list of time in format `[<hour>, <minute>]` to run script/command at a specific time

* `COMMAND`: here is the `bash` command that would be executed
