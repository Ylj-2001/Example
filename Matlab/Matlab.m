%%偏差
UT1=[1 2 3 4 5 6 7 8 9 10;3 6 9 2 5 8 1 4 7 10]'
CD2(UT1)
UT2=[1 2 3 4 5 6 7 8 9 10;7 4 1 8 5 2 9 6 3 10]'
CD2(UT2)
UT3=[1 2 3 4 5 6 7 8 9 10;9 8 7 6 5 4 3 2 1 10]'
CD2(UT3)
X=(2*UT1-1)/(2*n)

%%绘图
[x,y]=meshgrid(0:11);
plot(x,y,"k",y,x,"k");
axis equal;
axis([0 1 0 1]);
scatter(X(:,2),X(:,1),10)

%%线性约束区域绘图
L1=[1 0;1 1];
plot(L1(:,1),L1(:,2),);hold on
text('color','b');
L2=[0 1;1 1];
plot(L2(:,1),L2(:,2));hold on
text('color','b');
L3=[0.5 0;0 1];
plot(L3(:,1),L3(:,2));hold on
text(0.2,0.7,'2x_1+x_2=1','color','b');
L4=[0 0;1 2];
plot(L4(:,1),L4(:,2));hold on
text(0.5,0.5,'2x_1-x_2=0','color','b');

[X1,X2]=meshgrid(0:1:1,0:1:1);
idX1=(X1<1)&(X2<1);
X1=X1(idX1);
X2=X2(idX1);
k=convhull(X1,X2);
h=fill(X1(k),X2(k),'g');
set(h,'edgealpha',0,'facealpha',0.3)

%超平面
n=11
GLPM(n,2)
U=ans(:,:,4)
X=(2*U-1)/(2*n)
X(n,:)=[]

Y=zeros(n-1,3);

%y1
    for i=1:n-1
        if (0 < X(i,1))&&( X(i,1) < 0.25)
             Y(i,1)=(1+2*sqrt(X(i,1)))/4;
        elseif (0.25 <= X(i,1))&&(X(i,1) < 0.75)
            Y(i,1)=3/8+X(i,1)/2;
        elseif (0.75 <= X(i,1))&&(X(i,1) < 1)
            Y(i,1)=(2-sqrt(1-X(i,1)))/2;
        end
    end
    %y2
     for i=1:n-1
        if (0 < X(i,1))&&( X(i,1) < 0.25)
             Y(i,2)=(1+2*(X(i,2)-1)*sqrt(X(i,1)));
        elseif (0.25 <= X(i,1))&&(X(i,1) < 0.75)
            Y(i,2)=X(i,2);
        elseif (0.75 <= X(i,1))&&(X(i,1) < 1)
            Y(i,2)=2*X(i,2)*sqrt(1-X(i,1));
        end
     end
     %y3
     for i=1:n-1
        if (0 < X(i,1))&&( X(i,1) < 0.25)
             Y(i,3)=(X(i,2))*sqrt(X(i,1));
        elseif (0.25 <= X(i,1))&&(X(i,1) < 0.75)
            Y(i,3)=X(i,1)+X(i,2)/2-0.25;
        elseif (0.75 <= X(i,1))&&(X(i,1) < 1)
            Y(i,3)=1-(1-X(i,2))*sqrt(1-X(i,1));
        end
     end
y2=2+3*Y(:,1)+2*Y(:,2)-2*Y(:,3)     
%%点图

y1=Y(:,1);
y22=Y(:,2);
y3=Y(:,3);
A=2;
B=0.5;
C=-1;
n=[A,B,C];
[x,y]=meshgrid(0:0.05:1);
z=A*x+B*y-1;
mesh(x,y,z)
hold on;
scatter3(y1,y22,y3,'filled'); 

scatter(X(:,1),X(:,2))


%%%%%超椭球
n=11
GLPM(n,2)
U=ans(:,:,4)
X=(2*U-1)/(2*n)
X(n,:)=[]

Y=zeros(n-1,3);

%y1
    for i=1:n-1
        if (0 < X(i,1))&&( X(i,1) < 0.5)
             Y(i,1)=(1+2*sqrt(X(i,1)))/4;
        elseif (0.25 <= X(i,1))&&(X(i,1) < 0.75)
            Y(i,1)=3/8+X(i,1)/2;
        elseif (0.75 <= X(i,1))&&(X(i,1) < 1)
            Y(i,1)=(2-sqrt(1-X(i,1)))/2;
        end
    end
    %y2
     for i=1:n-1
        if (0 < X(i,1))&&( X(i,1) < 0.25)
             Y(i,2)=(1+2*(X(i,2)-1)*sqrt(X(i,1)));
        elseif (0.25 <= X(i,1))&&(X(i,1) < 0.75)
            Y(i,2)=X(i,2);
        elseif (0.75 <= X(i,1))&&(X(i,1) < 1)
            Y(i,2)=2*X(i,2)*sqrt(1-X(i,1));
        end
     end
     %y3
     for i=1:n-1
        if (0 < X(i,1))&&( X(i,1) < 0.25)
             Y(i,3)=(X(i,2))*sqrt(X(i,1));
        elseif (0.25 <= X(i,1))&&(X(i,1) < 0.75)
            Y(i,3)=X(i,1)+X(i,2)/2-0.25;
        elseif (0.75 <= X(i,1))&&(X(i,1) < 1)
            Y(i,3)=1-(1-X(i,2))*sqrt(1-X(i,1));
        end
     end
y2=2+3*Y(:,1)+2*Y(:,2)-2*Y(:,3)     

%%点图

y1=Y(:,1);
y22=Y(:,2);
y3=Y(:,3);
A=2;
B=0.5;
C=-1;
n=[A,B,C];
[x,y]=meshgrid(0:0.05:1);
z=A*x+B*y-1;
mesh(x,y,z)
hold on;
scatter3(y1,y22,y3,'filled'); 

scatter(X(:,1),X(:,2))


