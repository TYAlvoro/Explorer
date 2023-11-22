unsigned const short int KEYPAD_PIN = 0;//аналоговый порт для клавиатуры

void setup() {
  Serial.begin(9600);
  analogReadResolution(10);//все аналоговые значение будут в диапазоне 0...1023
}

void loop() {
  Serial.println(getPressedKeypadButton());//выводим номер нажатой кнопки в монитор порта
}

short int getPressedKeypadButton(){//считывает нажатия keypad`a
//возвращает значение от 1 до 16 в зависимости нажатой кнопки или 0 если ничего не нажато
  const int OCCURACY = 5;//ошибка в точности определения значений
  int sensorValue = analogRead(KEYPAD_PIN);//читаем значение с датчика
  int keys[] = {1016, 937, 860, 794, 683, 641, 604, 571, 509, 485, 464, 444, 407, 328, 275, 236};//массив примерных значений для клавиш(0-15, где 0=1, 1=2 и т.д.)
  if(sensorValue > -OCCURACY && sensorValue < OCCURACY){return 0;}//если ничего не нажато, то сразу возвращаем 0
  for(short int i = 0; i < 16; i++){//проверяем в цыкле с каким по номеру элементом массива совпадает значение с датчика
    if(sensorValue > (keys[i] - OCCURACY) && sensorValue < (keys[i] + OCCURACY)){
      return i+1;//возвращаем на один больше, т.к. при проверке у нас 0 считается первой кнопкой, но для удобства 0 будет отсутсвием сигнала
    }
  }
}
