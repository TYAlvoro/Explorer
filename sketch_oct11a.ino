int inButt1 = A5;
int inButt2 = A3;
int inButt3 = A3;
int numButt = 100;

void setup() 
{
  Serial.begin(9600);
}

void FirstKeyBoard()
{
    int varButt1 = analogRead(inButt1);
    if (varButt1 == 1023) {
      Serial.println("А");
      delay(300);
    }
    if (varButt1 == 930) {
      Serial.println("Б");
      delay(300);  
    }
    if (varButt1 == 853) {
      Serial.println("В");
      delay(300);  
    }
    if (varButt1 == 787) {
      Serial.println("Г");
      delay(300);  
    }
    if (varButt1 == 678) {
      Serial.println("Д");
      delay(300);  
    }
    if (varButt1 == 635) {
      Serial.println("Е");
      delay(300);  
    }
    if (varButt1 == 598) {
      Serial.println("Ё");
      delay(300);  
    }
    if (varButt1 == 565) {
      Serial.println("Ж");
      delay(300);  
    }
    if (varButt1 == 506) {
      Serial.println("З");
      delay(300);  
    }
    if (varButt1 == 482) {
      Serial.println("И");
      delay(300);  
    }
    if (varButt1 == 460) {
      Serial.println("Й");
      delay(300);  
    }
    if (varButt1 == 440) {
      Serial.println("К");
      delay(300);  
    }
    if (varButt1 == 404) {
      Serial.println("Л");
      delay(300);  
    }
    if (varButt1 == 325) {
      Serial.println("М");
      delay(300);  
    }
    if (varButt1 == 272) {
      Serial.println("Н");
      delay(300);  
    }
    if (varButt1 == 233) {
      Serial.println("О");
      delay(300);  
    }  
}

void SecondKeyBoard()
{

}
void loop() 
{ 
    FirstKeyBoard();
    SecondKeyBoard();
}
