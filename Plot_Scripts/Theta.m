close all;
%%FirstMovement
%%Rotation-Acceleration in Z-Axis
figure;
t1 =[0 5];
dudt21 =[0.0069813 0.0069813];
t2 = [5 13.283];
dudt22 = [0 0];
t3 = [13.283 18.283];
dudt23 = [-0.0069813 -0.0069813];
plot(t1,dudt21,'b');
hold on;
plot(t2,dudt22,'b');
hold on;
plot(t3,dudt23,'b');
xlabel('t (s)');ylabel('u"(t) (rad/s^2)');
title ("Plot of Robot's Desired Rotation-Acceleration In Z-Axis"); 
saveas(1,'PDRAZ.jpg');
%%Rotation-Velocity in Z-Axis
figure;
dudt1 = [0 0.034907];
dudt2 = [0.034907 0.034907];
dudt3 = [0.034907 0];
plot(t1,dudt1,'b');
hold on;
plot(t2,dudt2,'b');
hold on;
plot(t3,dudt3,'b');
xlabel('t (s)');ylabel("u'(t) (rad/s)");
title ("Plot of Robot's Desired Rotation-Velocity In Z-Axis"); 
saveas(2,'PDRVZ.jpg');
%%Rotation in Z-Axis
u1=0;
u2=atan2(10,20);
t1=0:0.1:5;
t2=5:0.1:13.283;
t3=13.1:0.1:18.283;
p1=[0.0034907 0 0];
figure;
plot(t1,polyval(p1,t1),'b');
hold on;
p2=[0.034907 0.087266]; % polynomial function
plot(t2,polyval(p2,t2-5),'b');
hold on;
p3=[-0.0034907 0 u2];% polynomial function
plot(t3,polyval(p3,18.283-t3),'b');
xlabel('t (s)');ylabel('u(t) (rad)');
title ("Plot of Robot's Desired Rotation In Z-Axis"); 
saveas(3,'PDRTZ.jpg');
%%SecondMovement
%%Rotation-Acceleration in Z-Axis
figure;
t1 =[0 5];
dudt21 =[0.017453 0.017453];
t2 = [5 23.313];
dudt22 = [0 0];
t3 = [23.313 28.313];
dudt23 = [-0.017453 -0.017453];
plot(t1,dudt21,'b');
hold on;
plot(t2,dudt22,'b');
hold on;
plot(t3,dudt23,'b');
xlabel('t (s)');ylabel('u"(t) (rad/s^2)');
title ("Plot of Robot's Desired Rotation-Acceleration In Z-Axis"); 
saveas(4,'PDRAZ2.jpg');
%%Rotation-Velocity in Z-Axis
figure;
dudt1 = [0 -0.087266];
dudt2 = [-0.087266 -0.087266];
dudt3 = [-0.087266 0];
plot(t1,dudt1,'b');
hold on;
plot(t2,dudt2,'b');
hold on;
plot(t3,dudt3,'b');
xlabel('t (s)');ylabel("u'(t) (rad/s)");
title ("Plot of Robot's Desired Rotation-Velocity In Z-Axis"); 
saveas(5,'PDRVZ2.jpg');
%%Position in Z-Axis
u1=atan2(10,20);
u2=atan2(-10-10,20-20);
t1=0:0.1:5;
t2=5:0.1:23.313;
t3=23.313:0.1:28.313;
p1=[-0.0087266 0 u1];
figure;
plot(t1,polyval(p1,t1),'b');
hold on;
p2=[-0.087266 u1-0.21817]; % polynomial function
plot(t2,polyval(p2,t2-5),'b');
hold on;
p3=[0.0087266 0 u2];% polynomial function
plot(t3,polyval(p3,28.313-t3),'b');
xlabel('t (s)');ylabel('u(t) (rad)');
title ("Plot of Robot's Desired Rotation In Z-Axis"); 
saveas(6,'PDRTZ2.jpg');
%%ThirdMovement
%%Rotation-Acceleration in Z-Axis
figure;
t1 =[0 5];
dudt21 =[0.069813 0.069813];
t2 = [5 10.23];
dudt22 = [0 0];
t3 = [10.23 15.23];
dudt23 = [-0.069813 -0.069813];
plot(t1,dudt21,'b');
hold on;
plot(t2,dudt22,'b');
hold on;
plot(t3,dudt23,'b');
xlabel('t (s)');ylabel('u"(t) (rad/s^2)');
title ("Plot of Robot's Desired Rotation-Acceleration In Z-Axis"); 
saveas(7,'PDRAZ3.jpg');
%%Rotation-Velocity in Z-Axis
figure;
dudt1 = [0 0.34907];
dudt2 = [0.34907 0.34907];
dudt3 = [0.34907 0];
plot(t1,dudt1,'b');
hold on;
plot(t2,dudt2,'b');
hold on;
plot(t3,dudt3,'b');
xlabel('t (s)');ylabel("u'(t) (rad/s)");
title ("Plot of Robot's Desired Rotation-Velocity In Z-Axis"); 
saveas(8,'PDRVZ3.jpg');
%%Position in Z-Axis
u1=atan2(-10-10,20-20);
u2=2;
t1=0:0.1:5;
t2=5:0.1:10.23;
t3=10.23:0.1:15.23;
p1=[0.034907 0 u1];
figure;
plot(t1,polyval(p1,t1),'b');
hold on;
p2=[0.34907 u1+0.87266];
plot(t2,polyval(p2,t2-5),'b');
hold on;
p3=[-0.034907 0 u2];
plot(t3,polyval(p3,15.23-t3),'b');
xlabel('t (s)');ylabel('u(t) (rad)');
title ("Plot of Robot's Desired Rotation In Z-Axis"); 
saveas(9,'PDRTZ3.jpg');