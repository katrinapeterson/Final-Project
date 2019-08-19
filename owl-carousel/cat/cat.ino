#include <Servo.h>                           // Include servo library
Servo servoRight;
Servo servoLeft;
int leftwhisker = 5;
int rightwhisker = 7;
int PIEZOPIN = 2;  
int buttonPin = 12;
// Declare pin that the piezo is connected to.
// DECLARE LED PINS HERE

// One octave of notes between A4 and A5, for Piezo Greeting
int note_A4 = 440;
int note_As4 = 466; int note_Bb4 = note_As4;
int note_B4 = 494;
int note_C5 = 523;
int note_Cs5 = 554; int note_Db5 = note_Cs5;
int note_D5 = 587;
int note_Ds5 = 622; int note_Eb5 = note_Ds5;
int note_E5 = 659;
int note_F5 = 698;
int note_Fs5 = 740; int note_Gb5 = note_Fs5;
int note_G5 = 784;
int note_Gs5 = 830; int note_Ab5 = note_Gs5;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(PIEZOPIN, OUTPUT);                 // Attach piezo to pin 3. 
  pinMode(rightwhisker, INPUT);
  pinMode(leftwhisker, INPUT);
  pinMode(buttonPin, INPUT);
  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);                     // Attach right signal to pin 12 
  // Attach LED pins here.
}

void loop() {
  // put your main code here, to run repeatedly:
  int leftinput = digitalRead(leftwhisker);
  int rightinput = digitalRead(rightwhisker);
  int buttoninput = digitalRead(buttonPin); 
  servoLeft.writeMicroseconds(1300);
  servoRight.writeMicroseconds(1700);
  if(leftinput == 0 && rightinput == 0){
    backup();
    rightturn();
  }else if(rightinput == 0){
    leftturn();
  }else if(leftinput == 0){
    rightturn();
  }
  if(buttoninput == 1){
    servoLeft.writeMicroseconds(1500);
    servoRight.writeMicroseconds(1500);
    delay(2000); 
    
    
  }
}
void leftturn(){
  servoRight.writeMicroseconds(1300);
  delay(1000);
}
void rightturn(){
  servoLeft.writeMicroseconds(1700);
  delay(1000);
}
void backup(){
  servoLeft.writeMicroseconds(1700);
  servoRight.writeMicroseconds(1300);
  delay(1000);
}
void turnaround(){
  
}
