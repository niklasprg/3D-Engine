import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    id: sliderPanel
    width: 200
    color: "#f0f0f0"
    border.color: "#cccccc"

    Column {
        anchors.fill: parent
        spacing: 10
        padding: 10

        Row {
            spacing: 5
            Text { text: "Camera Settings:" }
        }

        Row {
            spacing: 5
            width: parent.width
            Text { text: "X Rotation:"; }
            Slider { from: 0; to: 20000 }
        }

        Row {
            spacing: 5
            Text { text: "Y Rotation:" }
            Slider { from: 0; to: 20000 }
        }

        Row {
            spacing: 5
            Text { text: "Z Rotation:" }
            Slider { from: 0; to: 20000 }
        }

        Row {
            spacing: 5
            Text { text: "Roll:" }
            Slider { from: 0; to: 3600 }
        }

        Row {
            spacing: 5
            Text { text: "Pitch:" }
            Slider { from: 0; to: 3600 }
        }

        Row {
            spacing: 5
            Text { text: "Yaw:" }
            Slider { from: 0; to: 3600 }
        }

        Row {
            spacing: 5
            Text { text: " " }
        }

        Row {
            spacing: 5
            Text { text: "Cube Settings:" }
        }

        Row {
            spacing: 5
            Text { text: "X Rotation:" }
            Slider { from: 0; to: 20000 }
        }

        Row {
            spacing: 5
            Text { text: "Y Rotation:" }
            Slider { from: 0; to: 20000 }
        }

        Row {
            spacing: 5
            Text { text: "Z Rotation:" }
            Slider { from: 0; to: 20000 }
        }

        Row {
            spacing: 5
            Text { text: "Roll:" }
            Slider { from: 0; to: 3600 }
        }

        Row {
            spacing: 5
            Text { text: "Pitch:" }
            Slider { from: 0; to: 3600 }
        }

        Row {
            spacing: 5
            Text { text: "Yaw:" }
            Slider { from: 0; to: 3600 }
        }

        Row {
            spacing: 5
            Text { text: "Scale:" }
            Slider { from: 1; to: 10 }
        }

    }
}
