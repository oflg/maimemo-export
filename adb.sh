# 使用 ADB 快速复制墨墨数据库到电脑，仅适用于 Linux，手机需要 ROOT
# 不会使用千万别手贱尝试，这个脚本仅为了我自己方便而已

echo 333221 | sudo -S adb kill-server 1>/dev/null 2>&1
echo 333221 | sudo -S adb start-server 1>/dev/null 2>&1
if [[ $(adb devices | awk '{print $2}' | sed -n '2p') != device ]]; then
  echo 请在手机上同意调试
  exit 1
fi
adb shell su -c "cp -rf /data/data/com.maimemo.android.momo/databases/maimemo.v*.db /sdcard"
name=$(adb shell ls /sdcard | grep maimemo.v)
adb pull /sdcard/$name /home/ourongxing/Github/maimemo-export
adb shell rm /sdcard/$name
sed -i "1,/maimemo\..*db/{s/maimemo\..*db/$name/}" main.py
