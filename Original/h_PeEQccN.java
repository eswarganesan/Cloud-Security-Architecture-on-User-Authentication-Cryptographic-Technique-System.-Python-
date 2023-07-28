import java.io.*;
import java.util.*;

public class h{
public static void main(String[] args){
Scanner sc=new Scanner(System.in);

int a[]=new int[10];
int b[]=new int[a.length];

for(int i=0;i<a.length;i++){
System.out.print("Enter the num: ");
a[i]=sc.nextInt();
}

for(int i=0;i<a.length;i++){
System.out.print(a[i]+" ");
}
for(int i=0;i<a.length;i++){
b[i]=a[i];
}
System.out.println();
for(int i=0;i<b.length;i++){
System.out.print(b[i]+" ");
}
}}

