// insert arduino code here
#include <Servo.h>

Servo servo1;

int SERVO1_PIN_NUMBER = 9; // replace with servo1 pin number on arduino

float CURR_X = 0;
float CURR_Y = 0;

int CAPTURE_ZONE_X = -2;
int CAPTURE_ZONE_Y = 8;

bool MAGNET = true;

void setup()
{
    Serial.begin(9600);
    servo1.attach(SERVO1_PIN_NUMBER);
}

// what's running
void loop()
{

    if (Serial.available() > 0)
    {
        char receivedChar = Serial.read();
        Serial.println(receivedChar);
    }

    //   servo1.write(90) //turns motor to 90 degrees
    //   delay(1000) // delay for a second

    // use sensors to check for player moves
    // move piece if necessary
    // tap server to determine both of these things
}

// move a piece from one coordinate to another
void movePiece(int x1, int y1, int x2, int y2)
{
    if () // capture
    {
        moveSlider(x2, y2);
        toggleMagnet();
        moveSliderSlow(CAPTURE_ZONE_X, CAPTURE_ZONE_Y);
        if (CAPTURE_ZONE_Y == 7)
        {
            if (CAPTURE_ZONE_X == 9)
                CAPTURE_ZONE_X = 8;
            else if (CAPTURE_ZONE_X == 8)
                CAPTURE_ZONE_X = -1;
            else if (CAPTURE_ZONE_X == -1)
                CAPTURE_ZONE_X = -2;
            CAPTURE_ZONE_Y = 8;
        }
        else
        {
            --CAPTURE_ZONE_Y;
        }
    }
    else if () // castle king side (O - O)
    {
        if () // white
        {
            // move rook
            moveSlider(0, 7);
            toggleMagnet();
            moveSliderSlow(0, 5);
            toggleMagnet();

            // move king
            moveSlider(0, 4);
            toggleMagnet();
            moveSliderSlow(-1, 4);
            moveSliderSlow(0, 6);
            toggleMagnet();
        }
        else // black
        {
            // move rook
            moveSlider(7, 7);
            toggleMagnet();
            moveSliderSlow(7, 5);
            toggleMagnet();

            // move king
            moveSlider(7, 4);
            toggleMagnet();
            moveSliderSlow(8, 4);
            moveSliderSlow(7, 6);
            toggleMagnet();
        }
    }
    else if () // castle queen side (O - O - O)
    {
        if () // white
        {
            // move rook
            moveSlider(0, 0);
            toggleMagnet();
            moveSliderSlow(0, 2);
            toggleMagnet();

            // move king
            moveSlider(0, 4);
            toggleMagnet();
            moveSliderSlow(-1, 4);
            moveSliderSlow(0, 2);
            toggleMagnet();
        }
        else // black
        {
            // move rook
            moveSlider(7, 0);
            toggleMagnet();
            moveSliderSlow(7, 2);
            toggleMagnet();

            // move king
            moveSlider(7, 4);
            toggleMagnet();
            moveSliderSlow(8, 4);
            moveSliderSlow(7, 2);
            toggleMagnet();
        }
    }
    else
    {
        // normal case
        moveSlider(x1, y1);
        toggleMagnet();

        moveSliderSlow(x2, y2);
        toggleMagnet();
    }
}

void toggleMagnet()
{
    MAGNET = !MAGNET;
}

// move from currX and currY to x,y
void moveSlider(int x, int y)
{
}

// move slowly from currX and currY to x,y
void moveSliderSlow(float x, float y)
{
}