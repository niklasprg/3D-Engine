import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Window {
    id: window

    color: "white"
    width: 1280
    height: 720

    minimumWidth: 852
    minimumHeight: 480

    visible: true
    title: "3D - Engine"

    Rectangle {
            id: mainContent
            anchors.fill: parent
            color: "white"

            Header {
                id: header
                anchors.top: parent.top
                anchors.left: parent.left
                anchors.right: parent.right
            }

            SliderPanel {
                id: sliderPanel
                visible: false
                anchors.left: parent.left
                anchors.top: header.bottom
                anchors.bottom: parent.bottom
            }
        }
}
