if [ -d "/home/$USER/.config/PERIODIC_JOB_MANAGER" ]; then
	rm /home/$USER/.config/PERIODIC_JOB_MANAGER -r
fi

cp CONFIG/ /home/$USER/.config/PERIODIC_JOB_MANAGER -r

if [ ! -d "/home/$USER/.config/autostart" ]; then
	mkdir /home/$USER/.config/autostart
fi

if [ -f "/home/$USER/.config/autostart/periodic_job_manager.desktop" ]; then
	rm /home/$USER/.config/autostart/periodic_job_manager.desktop
fi

cp AUTORUN/periodic_job_manager.desktop /home/$USER/.config/autostart/periodic_job_manager.desktop

if [ -d "/home/$USER/.PERIODIC_JOB_MANAGER" ]; then
	rm /home/$USER/.PERIODIC_JOB_MANAGER -r
fi

cp PERIODIC_JOB_MANAGER /home/$USER/.PERIODIC_JOB_MANAGER -r
cp ICONS /home/$USER/.PERIODIC_JOB_MANAGER/ICONS -r
