#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion
from nav_msgs.msg import Odometry
from math import pow,atan2,sqrt,sin,cos,pi

# Student : Papakostas Ioannis , AM : 4143
class p3dxRobotController:

    def __init__(self):
    
        # Here i create a unique node with name p3dxRobot_controller
        rospy.init_node('p3dxRobot_controller', anonymous=True)
        # Here i create a Publisher which will publish to the topic /RosAria/cmd_vel
        self.velocity_publisher = rospy.Publisher('/RosAria/cmd_vel',Twist, queue_size=10)
        # Here i create a Subscriber which will subscribe to the topic /RosAria/pose
        self.pose_subscriber = rospy.Subscriber('/RosAria/pose',Odometry,self.update_position)
        # Here i create an object of Odometry for taking the robot's current position
        self.odom = Odometry()
        # Here i initialize the publish rate in 10 Hz
        self.rate = rospy.Rate(10)
    
    # Here is a method which is called when a message of type Odometry arrives and here i update robot's current position  
    def update_position(self,odom_data):
    
        self.odom.header.stamp = rospy.get_rostime().to_sec()
        self.odom.header.frame_id = "odom"
        self.odom.pose.pose.position.x = odom_data.pose.pose.position.x
        self.odom.pose.pose.position.y = odom_data.pose.pose.position.y
    	rot_q = odom_data.pose.pose.orientation
    	(roll, pitch, self.odom.pose.pose.orientation.z) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
    
    # Here is a method for calculating the distance between robot's current position and goal position
    def distance_calculator(self,goal_odom):
    
        return sqrt(pow((goal_odom.pose.pose.position.x - self.odom.pose.pose.position.x), 2) + pow((goal_odom.pose.pose.position.y - self.odom.pose.pose.position.y), 2))
    
    # Here is a method for calculating next robot's linear velocity in x-axis
    def linear_velocity_calculator(self,acceleration,time):
        
        return time * acceleration
    
    # Here is a method for calculating next robot's angular velocity in z-axis
    def angular_velocity_calculator(self,acceleration,time):
        
        return time * acceleration    
    
    # Here is a method for calculating the condition for the part of stable velocity in method of linear-functions with parabolic parts (method angular_position_achivement)
    def angular_condition_calculator(self,desired_angle,initial_angle):
        
        if(desired_angle>initial_angle):
            return desired_angle-initial_angle >= self.odom.pose.pose.orientation.z 
        else:
            return desired_angle-initial_angle <= self.odom.pose.pose.orientation.z
    
    # Here is a method for finding a suitable tb for method of linear-functions with parabolic parts(linear movement)
    def linear_movement_suitable_tb_calculator(self,goal_odom,time):
        
        # Here is the max linear speed(m/s)
        mls = 0.4
        # Here i calculate a suitable time
        suitable_time = ((self.distance_calculator(goal_odom))/mls)/4 # I calculate the suitable time with this type : (linear_distance/maximum_linear_speed)/4
        
        #Here i calculate the movement in tb=time
    	db = 0.5*mls*time
        
        # Here i check the time that user has chosen and i change it if it isn't suitable
        if((self.distance_calculator(goal_odom)/2) <= db):
            return suitable_time
        else:
            return time
        
    # Here is a method for finding a suitable tb for method of linear-functions with parabolic parts(angular movement)
    def angular_movement_suitable_tb_calculator(self,goal_odom,velocity,time,true):
        
        # Here is the max angular speed(rad/s)
        mas = velocity*2*(pi)/360
        # Here i initialize the initial z-orientation of robot 
    	z0 = self.odom.pose.pose.orientation.z
        
        if(true==1): # Here i give a desired z-orientation   
            # Here i initialize the desired z-orientation of robot 
         	zan = goal_odom.pose.pose.orientation.z 
        else: # Here i calculate the desired z-orientation for moving to the desired spot of x-y-level 
            # Here i initialize the desired z-orientation of robot 
         	zan = atan2(goal_odom.pose.pose.position.y-self.odom.pose.pose.position.y,goal_odom.pose.pose.position.x-self.odom.pose.pose.position.x)
        
        # Here i calculate the desired rotation of my robot
        if(zan>z0):
            zan = atan2(goal_odom.pose.pose.position.y-self.odom.pose.pose.position.y,goal_odom.pose.pose.position.x-self.odom.pose.pose.position.x)- z0
        else:
            zan = z0 - atan2(goal_odom.pose.pose.position.y-self.odom.pose.pose.position.y,goal_odom.pose.pose.position.x-self.odom.pose.pose.position.x)
         
        # Here i calculate a suitable time
        suitable_time = (zan/mas)/4 # I calculate the suitable time with this type : (rotation/maximum_angular_speed)/4
    	
    	#Here i calculate the rotation in tb=time
    	zb = 0.5*mas*time

        # Here i check the time that user has chosen and i change it if it isn't suitable
        if(zan/2 <= zb):
            return suitable_time
        else:
            return time
        
        
    # Here is a method for achiving the desired rotation in z-axis
    def angular_position_achivement(self,time,goal_odom,velocity,true):
    	
    	 # Here is the max angular speed(rad/s)
         mas = velocity*2*(pi)/360 
         # Here i calculate the acceleration so as to have the maximum angular speed in time tb
         at = mas/time  
    	 # Here i initialize the initial z-orientation of robot 
    	 z0 = self.odom.pose.pose.orientation.z
         
         if(true==1): # Here i give a desired z-orientation   
            # Here i initialize the desired z-orientation of robot 
         	zan = goal_odom.pose.pose.orientation.z 
         else: # Here i calculate the desired z-orientation for moving to the desired spot of x-y-level 
            # Here i initialize the desired z-orientation of robot 
         	zan = atan2(goal_odom.pose.pose.position.y-self.odom.pose.pose.position.y,goal_odom.pose.pose.position.x-self.odom.pose.pose.position.x)
         
         # Here i check if my robot should rotate clockwise or anticlockwise 
         if(zan>z0):
            pros = 1 # anticlockwise
         else:
            pros = -1 # clockwise
         
         # Here i calculate the initial time 
         t0 = rospy.get_rostime().to_sec()
         # I use 2 helping time variables which are initialized in t0
         t1 = t0
         t2 = t0
         
         # Here i create a Twist object for velocity commands and i initialize the velocities
         vel_msg = Twist()
         vel_msg.linear.x = 0
         vel_msg.linear.y = 0
         vel_msg.linear.z = 0
         vel_msg.angular.x = 0
         vel_msg.angular.y = 0
         
    	 while(1): # Here i implement the desired rotation
            
            if((at*time>at*(t1-t0))): # Here i implement the part of stable acceleration in method of linear-functions with parabolic parts
                
                # Here i take the current_time
                t1 = rospy.get_rostime().to_sec()
                # Here i call the angular_velocity_calculator method for giving in robot the correct velocity	
                vel_msg.angular.z = pros*self.angular_velocity_calculator(at,t1-t0)
                # Here i publish the desired vel_msg
                self.velocity_publisher.publish(vel_msg)
                # Here i take the rotation in z-axis that robot has done so far 
                db = self.odom.pose.pose.orientation.z - z0
            
            elif(self.angular_condition_calculator(zan,db)): # Here i implement the part of stable velocity in method of linear-functions with parabolic parts
               
                # Here i call the angular_velocity_calculator method for giving in robot the correct velocity
                vel_msg.angular.z = pros*self.angular_velocity_calculator(at,time)
                # Here i publish the desired vel_msg
                self.velocity_publisher.publish(vel_msg)
                # Here i take the time that has elapsed so far
                t2 = rospy.get_rostime().to_sec()
            
            else:  # Here i implement the part of stable deceleration in method of linear-functions with parabolic parts 
                
                # Here i take the current_time
                t1 = rospy.get_rostime().to_sec()
                # Here i call the angular_velocity_calculator method for giving in robot the correct velocity
                vel_msg.angular.z = pros*(self.angular_velocity_calculator(at,time) - self.angular_velocity_calculator(at,t1-t2))
                # Here i check if my velocity has the opposite of the desired direction
                if((pros>0) and (vel_msg.angular.z<0)):
                	break
                elif((pros<1) and (vel_msg.angular.z>0)):
                	break	
                # Here i  publish the desired vel_msg
                self.velocity_publisher.publish(vel_msg)
            
            # Here i publish at the desired rate
            self.rate.sleep()   
    	 
         # Here i set angular speed in z-axis to 0 and i publish the desired vel_msg
         vel_msg.angular.z = 0
    	 self.velocity_publisher.publish(vel_msg)
         
    # Here is a method for achiving the desired movement in x-y-level     
    def xy_position_achivement(self,time,goal_odom):
         
         # Here is the max linear speed(m/s)
         mls = 0.4
         # Here i calculate the a so as to have the maximum linear speed in time tb
         a = mls/time 
     
         # Here i take the initial position of robot in x-axis  
         x0 = self.odom.pose.pose.position.x
         # Here i take the initial position of robot in y-axis
         y0 = self.odom.pose.pose.position.y

         # Here i calculate the distance between desired  and current position of robot in x-y-level 
         distance = self.distance_calculator(goal_odom);
         
         # Here i calculate the initial time 
         t0 = rospy.get_rostime().to_sec()
         # Here i use 2 helping time variables which are initialized in t0
         t1 = t0
         t2 = t0
         
         # Here i create a Twist object for velocity commands and i initialize the velocities
         vel_msg = Twist()
         vel_msg.linear.y = 0
         vel_msg.linear.z = 0
         vel_msg.angular.x = 0
         vel_msg.angular.y = 0 
         vel_msg.angular.z = 0 
         
    	 while(1) : # Here i implement the movement to the desired position in x-y-level 
         
           if((a*time>a*(t1-t0))): # Here i implement the part of stable acceleration in method of linear-functions with parabolic parts
                
                # Here i take the current_time
                t1 = rospy.get_rostime().to_sec()
                # Here i call the linear_velocity_calculator method for giving in robot the correct velocity	
                vel_msg.linear.x = self.linear_velocity_calculator(a,t1-t0)
                # Here i  publish the desired vel_msg
                self.velocity_publisher.publish(vel_msg)
                # Here i take the distance that robot has done so far 
                db = distance - self.distance_calculator(goal_odom)
            
           elif(self.distance_calculator(goal_odom)>db): # Here i implement the part of stable velocity in method of linear-functions with parabolic parts
               
                # Here i call the linear_velocity_calculator method for giving in robot the correct velocity
                vel_msg.linear.x = self.linear_velocity_calculator(a,time)
                # Here i publish the desired vel_msg
                self.velocity_publisher.publish(vel_msg)
                # Here i take the time that has elapsed so far   
                t2 = rospy.get_rostime().to_sec()
           
           else: # Here i implement the part of stable deceleration in method of linear-functions with parabolic parts
                
                # Here i take the current_time
                t1 = rospy.get_rostime().to_sec()
                # Here i call the linear_velocity_calculator for giving in robot the correct velocity
                vel_msg.linear.x = self.linear_velocity_calculator(a,time)-self.linear_velocity_calculator(a,t1-t2)
                # Here i check if my velocity has the opposite of desired direction
                if(vel_msg.linear.x<0):
                	break
                # Here i publish the desired vel_msg
                self.velocity_publisher.publish(vel_msg)
            
           #Here i publish at the desired rate.
           self.rate.sleep() 
         
         #Here i set linear speed in x-axis to 0 and i publish the desired vel_msg 
         vel_msg.linear.x = 0
         self.velocity_publisher.publish(vel_msg)
         
    #Here is a method for moving the robot to the desired position  
    def movetodesiredgoal(self):
    
    	# Here i initialize the time of first part of method of linear-functions with parabolic parts(I have chosen this time for the graphs to be as clear as possible)
        time = 5
        
        AM = 4143
        
        # Here i initialize the robot's final position 
        goal_odom = Odometry() 
        goal_odom.header.stamp = rospy.get_rostime()
        goal_odom.header.frame_id = "odom"
        # The intermediate and the final position in x-axis should be round(AM/200) m
        goal_odom.pose.pose.position.x = round(AM/200,4)
        # The intermediate position in y-axis should be round((AM/2)/200) m 
        goal_odom.pose.pose.position.y = round(AM/400,4)
        # The final z-orientation should be (AM/2)/1000 rad
        goal_odom.pose.pose.orientation.z = AM/2000
        # The final position in y-axis should be -round((AM/2)/200) m
        finaly = (-1)*goal_odom.pose.pose.position.y
        
        # Here i implement the first part of movement(q0 to qu)
        
        velocity = 2 # The angular_velocity is 2 deg/sec (I have chosen this angular velocity for the graphs to be as clear as possible)
        time1 = self.angular_movement_suitable_tb_calculator(goal_odom,velocity,time,0) # Here i check if the time is suitable,otherwise i change it with a suitable one 
        self.angular_position_achivement(time1,goal_odom,velocity,0) # Here i call a method that will achive the intermediate z-orientation 
         
        time2 = self.linear_movement_suitable_tb_calculator(goal_odom,time) # Here i check if the time is suitable,otherwise i change it with a suitable one
        self.xy_position_achivement(time2,goal_odom) # Here i call a method that will achive the intermediate position in x-axis and y-axis
        
        # Here i implement the second part of movement(qu to qf)
        
        # Here i change the goal_odom.pose.pose.position.y in the finaly 
        goal_odom.pose.pose.position.y = finaly
        
        velocity = 5 # The angular_velocity is 5 deg/sec (I have chosen this angular velocity for the graphs to be as clear as possible) 
        time3 = self.angular_movement_suitable_tb_calculator(goal_odom,velocity,time,0) # Here i check if the time is suitable,otherwise i change it with a suitable one
        self.angular_position_achivement(time3,goal_odom,velocity,0) # Here i call a method that will achive the intermediate z-orientation 
        
        time4 = self.linear_movement_suitable_tb_calculator(goal_odom,time) # Here i check if the time is suitable,otherwise i change it with a suitable one
        self.xy_position_achivement(time4,goal_odom) # Here i call a method that will achive the final position in x-axis and y-axis
        
        velocity = 20 # The angular_velocity is 20 deg/sec (I have chosen this angular velocity for the graphs to be as clear as possible)
        time5 = self.angular_movement_suitable_tb_calculator(goal_odom,velocity,time,1) # Here i check if the time is suitable,otherwise i change it with a suitable one
        self.angular_position_achivement(time5,goal_odom,velocity,1) # Here i call a method that will achive the final z-orientation 
        
        print("Real position in x-axis",self.odom.pose.pose.position.x,"Desired Position in x-axis",goal_odom.pose.pose.position.x,"Real position in y-axis",self.odom.pose.pose.position.y,"Desired position in y-axis",goal_odom.pose.pose.position.y,"Real rotation in z-axis",self.odom.pose.pose.orientation.z,"Desired rotation in z-axis",goal_odom.pose.pose.orientation.z)
        
        # Here if i press control + C, the node will stop
        rospy.spin()

if __name__ == '__main__':
    try:
        myRosariaController = p3dxRobotController()
        myRosariaController.movetodesiredgoal()
    except rospy.ROSInterruptException:
        pass