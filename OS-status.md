# Capport support status

2023/9/30

Test and investigation results are shown below. They might be different from vendors' official statements. (CP=Captive Portal)

## Android
- Android 11 and newer: Capport API (RFC 8908) is supported.
- Android 12 (Pixel 3): CP works well. Notification with icon is available even when CP is disabled ("captive": false).
- Android 13 (Pixel 7 and 7 Pro): CP works well. Notification with icon is available even when CP is disabled.
- Android 11 (Galaxy A21): 
CP works well. Notification with icon is available even when CP is disabled.
- Android 12 (Galaxy A41): CP works well. Notification with icon is available even when CP is disabled.

- Android 10 and older: No support. (Vendor-specific CP only)

## iOS/iPadOS
- iOS/iPadOS 17: Capport API (RFC 8908) is supported.
- iOS/iPadOS 17: When CP is enabled, popup window appears. However, when CP is disabled, there is no notification. "Open Portal Page" link appears in the Wi-Fi setting menu.

- iOS/iPadOS 16 and older: No support. (Vendor-specific CP only)

## macOS
- macOS 13 (Ventura) and newer: Capport API (RFC 8908) is supported.
- Ventura and Sonoma: CP works well, but there is no Venue Info notification when CP is disabled.

- macOS 12 (Monterey) and older: No support. (Vendor-specific CP only)

## Windows
- Windows 10/11: No support. (Vendor-specific CP only) In fact, no API call is observed.

## ChromeOS
- ChromeOS: No support. No API call is observed (confirmed with version 115 and 117).


