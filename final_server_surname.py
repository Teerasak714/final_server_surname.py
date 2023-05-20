supawit@supawit:~$ import rospy

Command 'import' not found, but can be installed with:

sudo apt install graphicsmagick-imagemagick-compat  # version 1.4+really1.3.35-1ubuntu0.1, or
sudo apt install imagemagick-6.q16                  # version 8:6.9.10.23+dfsg-2.1ubuntu11.7
sudo apt install imagemagick-6.q16hdri              # version 8:6.9.10.23+dfsg-2.1ubuntu11.7

supawit@supawit:~$ from std_srvs.srv import Empty
from: can't read /var/mail/std_srvs.srv
supawit@supawit:~$ 
supawit@supawit:~$ def handle_request(request):
bash: syntax error near unexpected token `('
supawit@supawit:~$     rospy.loginfo("Hi, My name is <Teerasak Wirakiat>")
bash: syntax error near unexpected token `"Hi, My name is <Teerasak Wirakiat>"'
supawit@supawit:~$     return []
bash: return: []: numeric argument required
bash: return: can only `return' from a function or sourced script
supawit@supawit:~$ 
supawit@supawit:~$ def server_surname():
bash: syntax error near unexpected token `('
supawit@supawit:~$     # กำหนดชื่อโหนดและเริ่มต้นใช้งานโหนด ROS
supawit@supawit:~$     rospy.init_node('surname_server')
bash: syntax error near unexpected token `'surname_server''
supawit@supawit:~$ 
supawit@supawit:~$     # สร้าง Service Server โดยระบุชื่อ Service, ชนิดของ Service, และฟังก์ชัน callback
supawit@supawit:~$     service = rospy.Service('/hi_sur', Empty, handle_request)
bash: syntax error near unexpected token `('
supawit@supawit:~$ 
supawit@supawit:~$     rospy.loginfo("Ready to receive surname request.")
bash: syntax error near unexpected token `"Ready to receive surname request."'
supawit@supawit:~$ 
supawit@supawit:~$     rospy.spin()
> 
> if name == '_main_':
>     server_surname()
