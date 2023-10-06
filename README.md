# VenueInfoHandler (experimental)
API/CGI for Venue Information notification on Public Wi-Fi to help users reach out to the portal site at the venue.

This helper is specialized for Venue Information display rather than Captive Portal that blocks the network usage. There is no access control at all. Our intention is to improve user engagement while allowing people to use the network continuously.

## Supported platforms

Please see also [Capport support status](OS-status.md).

### Modern Capport (RFC 8908/8910)
- Android 11+
- iOS/iPadOS 17+
- macOS 13 (Ventura)+

### Vendor-specific Captive Portal
- iOS/iPadOS 16 and some older ones
- macOS 12 (Montrerey) and some older ones


## Specifications
- Capport API (RFC 8908/8910) is the primary, while vendor-specific methods are optional.
- Usable with Open, PSK, 802.1X, and Passpoint networks.
- Support (partly) Apple's legacy Captive Portal mechanism (CNA, Captive Network Assistant).

## Requirements
- Redis
- Perl
- (Local) HTTP server with a server certificate issued by a popular CA
- Local DNS server
- DHCP server

## Limitations
- (Disturbing) Captive Portal is enforced on Apple devices since they haven't got a nice notification mechanism.
- No support for Android 10 and older.
- No support for Windows 10/11 so far.
- Not working well over NAPT. To overcome this, we will need a DHCP server that can attach some paramters like MAC address in order for the API to uniquely identify the user device behind a NAPT box.

## Website layout
- https://\<portal.example.com\>/ -- Portal site of the venue. (SSL is required)
- https://\<example.net\>/cp/ -- Capport API (SSL is required)
- http://\<local IP address\>/ -- Diverted destination for Apple's legacy captive portal mechanism. (No SSL)

## Configuration
- Edit capport.cfg and index.cgi in cp/.
- Make sure all required modules exist. (Do perl -c api.cgi for example.)
- Setup Apache HTTP server or alternative.
- Setup Redis.
- Setup local DNS server. Dnsmasq is a handy DNS server for overriding domain names.
- To enable Captive Portal API (Capport API) for Android 11+ and Apple devices, add an DHCP option 114 as follows (Dnsmasq case).
-- dhsp-option~114,https://example.com/cp/api.cgi&cp=0
- (to be added)
