import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQuick.Layouts 1.14


//  Main window
ApplicationWindow
{
    property bool counting: false
    property bool soundOn: true

    id: root
    visible: true
    title: "PRJ001  |   Productivity Clock"
    color: "#242424"

    minimumWidth: 768
    minimumHeight: 432



    ColumnLayout
    {
        anchors.fill: parent

        //  Time display
        //  Also supports period editing when not counting
        TextField
        {
            id: timeField
            Layout.alignment: Qt.AlignHCenter
            implicitWidth: 400

            text: "00:20:00"
            font.family: "Sawasdee"
            font.pointSize: 60
            color: "white"
            horizontalAlignment: Text.AlignHCenter


            background: Rectangle { border.width: 0; color: "#242424" }
        }



        //  Start/Stop button
        Button
        {
            id: timerToggle
            Layout.alignment: Qt.AlignHCenter

            text: counting ? "Stop" : "Start"
            font.family: "Sawasdee"
            font.pointSize: 16

            onClicked: toggleHandler()
        }



        //  Toggle sound
        Button
        {
            id: soundToggle
            implicitWidth: 100
            implicitHeight: 30
            Layout.alignment: Qt.AlignHCenter

            contentItem: Text
            {
                horizontalAlignment: Text.AlignHCenter
                text: soundOn ? "Sound: On" : "Sound: Off"
                color: "white"
            }

            background: Rectangle { opacity: 0.1 }

            onClicked:
            { soundOn = !soundOn; manager.toggleSound(soundOn); }
        }
    }



    //  Start/Stop button click handler
    function toggleHandler()
    {
        //  Change counting state
        counting = !counting;


        if (counting)
        {
            timeField.readOnly = true;
            manager.setPeriod(timeField.text);
        }
        else
        {
            timeField.readOnly = false;
            timeField.text = manager.getPeriod();
        }

        manager.toggleTimer(counting);
    }



    //  Update signal handler
    //  Updates time display text from signal value
    function updateTime(val)
    { timeField.text = val; }
}