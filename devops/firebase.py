
import os
import firebase_admin
from firebase_admin import credentials, messaging

# Inicializar Firebase
cred = credentials.Certificate(
    os.environ["FIREBASE_CREDENTIALS"]
)

firebase_admin.initialize_app(cred)


def send_popup(device_token, title, message):
    """
    Envía una notificación push a Android.
    """

    notification = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=message
        ),
        android=messaging.AndroidConfig(
            priority="high",
            notification=messaging.AndroidNotification(
                channel_id="alerts",
                sound="default",
                priority="high"
            )
        ),
        token=device_token
    )

    try:
        response = messaging.send(notification)
        print("Notification sent:", response)
        return True

    except firebase_admin.exceptions.FirebaseError as error:
        print("Firebase error:", error)
        return False


if __name__ == "__main__":

    token = os.environ["FCM_DEVICE_TOKEN"]

    send_popup(
        device_token=token,
        title="System Alert",
        message="Your application requires attention."
    )
