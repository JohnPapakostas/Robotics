% Onoma : Papakostas Ioannis , AM : 4143
close all;
%%FirstMovement
%%Acceleration in X-Axis
figure;
t1 =[0 5];
dxdt21 =[0.071554 0.071554];
t2 = [5 55.902];
dxdt22 = [0 0];
t3 = [55.902 60.902];
dxdt23 = [-0.071554 -0.071554];
plot(t1,dxdt21,'b');
hold on;
plot(t2,dxdt22,'b');
hold on;
plot(t3,dxdt23,'b');
xlabel('t (s)');ylabel('x"(t) (m/s^2)');
title ("Plot of Robot's Desired Acceleration In X-Axis"); 
saveas(1,'PDAX.jpg');
%%Acceleration in Y-Axis
figure;
dydt21 =[0.035778 0.035778];
dydt22 = [0 0];
dydt23 = [-0.035778 -0.035778];
plot(t1,dydt21,'b');
hold on;
plot(t2,dydt22,'b');
hold on;
plot(t3,dydt23,'b');
xlabel('t (s)');ylabel('y"(t) (m/s^2)');
title ("Plot of Robot's Desired Acceleration In Y-Axis"); 
saveas(2,'PDAY.jpg');
%%Velocity in X-Axis
figure;
dxdt1 = [0 0.35777 ];
dxdt2 = [0.35777 0.35777];
dxdt3 = [0.35777 0];
plot(t1,dxdt1,'b');
hold on;
plot(t2,dxdt2,'b');
hold on;
plot(t3,dxdt3,'b');
xlabel('t (s)');ylabel("x'(t) (m/s)");
title ("Plot of Robot's Desired Velocity In X-Axis"); 
saveas(3,'PDVX.jpg');
%%Velocity in Y-Axis
figure;
dydt1 =[0 0.17889];
dydt2 =[0.17889 0.17889];
dydt3 =[0.17889 0];
plot(t1,dydt1,'b');
hold on;
plot(t2,dydt2,'b');
hold on;
plot(t3,dydt3,'b');
xlabel('t (s)');ylabel("y'(t) (m/s)");
title ("Plot of Robot's Desired Velocity In Y-Axis"); 
saveas(4,'PDVY.jpg');
%%Position in X-Axis
x1=0;
x2=20;
t1=0:0.1:5;
t2=5:0.1:55.902;
t3=55.902:0.1:60.902;
p1=[0.035777 0 0];
figure;
plot(t1,polyval(p1,t1),'b');
hold on;
p2=[0.35777 0.89443]; % polynomial function
plot(t2,polyval(p2,t2-5),'b');
hold on;
p3=[-0.035777 0 x2];% polynomial function
plot(t3,polyval(p3,60.902-t3),'b');
xlabel('t (s)');ylabel('x(t) (m)');
title ("Plot of Robot's Desired Position In X-Axis"); 
saveas(5,'PDTX.jpg');
%%Position in Y-Axis
y1=0;
y2=10;
p1=[0.017889 0 0];
figure;
plot(t1,polyval(p1,t1),'b');
hold on;
p2=[0.17889 0.447225];
plot(t2,polyval(p2,t2-5),'b');
hold on;
p3=[-0.017889 0 y2];
plot(t3,polyval(p3,60.902-t3),'b');
xlabel('t (s)');ylabel('y(t) (m)');
title ("Plot of Robot's Desired Position In Y-Axis"); 
saveas(6,'PDTY.jpg');
%%SecondMovement
%%Acceleration in Y-Axis
figure;
t1 =[0 5];
t2 =[5 50];
t3 =[50 55];
dydt21 =[-0.08 -0.08];
dydt22 = [0 0];
dydt23 = [0.08 0.08];
plot(t1,dydt21,'b');
hold on;
plot(t2,dydt22,'b');
hold on;
plot(t3,dydt23,'b');
xlabel('t (s)');ylabel('y"(t) (m/s^2)');
title ("Plot of Robot's Desired Acceleration In Y-Axis"); 
saveas(7,'PDAY2.jpg');
%%Velocity in Y-Axis
figure;
dydt1 =[0 -0.4];
dydt2 =[-0.4 -0.4];
dydt3 =[-0.4 0];
plot(t1,dydt1,'b');
hold on;
plot(t2,dydt2,'b');
hold on;
plot(t3,dydt3,'b');
xlabel('t (s)');ylabel("y'(t) (m/s)");
title ("Plot of Robot's Desired Velocity In Y-Axis"); 
saveas(8,'PDVY2.jpg');
%%Position in Y-Axis
y1=10;
y2=-10;
t1=0:0.1:5;
t2=5:0.1:50;
t3=50:0.1:55;
p1=[-0.04 0 10];
figure;
plot(t1,polyval(p1,t1),'b');
hold on;
p2=[-0.4 9];
plot(t2,polyval(p2,t2-5),'b');
hold on;
p3=[0.04 0 y2];
plot(t3,polyval(p3,55-t3),'b');
xlabel('t (s)');ylabel('y(t) (m)');
title ("Plot of Robot's Desired Position In Y-Axis"); 
saveas(9,'PDTY2.jpg');




