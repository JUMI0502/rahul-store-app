## Before You Start
Request the following from the project owner before setup:
- `x-api-key` value for backend requests
- Confirm you have: Node.js, Android Studio + Android SDK, a physical
  Android device (or emulator) with Google Play Services

## Requirements
- Node.js v25.9.0 (or compatible)
- JDK 21
- Android Studio with SDK installed
- Do NOT install a global `expo-cli` — this project uses the local Expo CLI
  automatically via `npx expo`, per the commands in this README

## Questions or Blockers
Contact Amini Masthan Reddy (aminimasthanreddy@gmail.com) if setup fails or
this README is outdated.# New Rahul Auto Spares — Store App

React Native (Expo SDK 54) staff-facing app for managing orders, stock,
staff, and mechanic approvals.

## Local Setup
```bash
git clone <repo-url>
cd rahul-store-app
npm install
```

You'll need `google-services.json` (Firebase config) placed in the project
root — get this from the team lead if not already present.

## Running (development build — required, Expo Go will NOT work)
This app uses custom native modules (including a full-screen order alert
feature and camera-based scanning) and cannot run in Expo Go.
```bash
npx expo prebuild --clean
npx expo run:android
```
Requires a physical Android device connected via USB (or emulator) and
Android Studio / SDK installed locally.

## Test Accounts (PIN login)
| Name | Role | PIN | Notes |
|---|---|---|---|
| Abdul Azeess | Owner | 9642 | Full access to all screens |
| Chand Basha | Senior | 9704 | Most owner permissions except some settings |
| Masha | Staff | 8919 | Limited access — no Staff Manager, Mechanic Approvals, etc. |
| Hussain Basha | Staff | 4444 | Same as above |
| Khaja | Staff | 1234 | Same as above |

## What to Test

### Core (Orders, Stock, Staff)
- Order lifecycle: New → Packing → Ready → Collected
- Push notification: place a test order from the customer app, confirm "New
  Order!" arrives even with this app closed
- Staff Manager (owner/senior only): Add, Edit, Delete, Reset PIN
- Stock: adjust quantity, mark items **OEM vs Generic/Compatible** (new)
- Scanner tab: scan a customer's order QR code → "Mark as Collected"
- Clock In / Clock Out (Attendance)

### New features (all under Reports tab, owner/senior only)
- **Mechanic Approvals**: approve/reject/edit/delete pending mechanic
  registrations submitted from the customer app
- **Service Reminders**: review customers 60+ days since last order, send a
  WhatsApp nudge with one tap
- **Warranty & Returns**: log a defect claim (product, customer, issue),
  resolve as replaced/refunded/repaired, or reject
- **Abandoned Carts**: see customers who added items but never checked out
  (3+ hours idle), send a WhatsApp nudge listing their cart contents
- **Sales Dashboard → Business Health section**: private staff productivity
  counts (not a public leaderboard), warranty claim rate, customer retention
- **Purchase Orders → Forecast tab**: products projected to run out within 7
  days based on actual 30-day sales velocity, not just a flat stock count
- **Add Product → Scan Barcode**: scan a product barcode to auto-check for
  duplicates or pre-fill the SKU field

### Removed (intentionally, part of professional redesign)
- Staff leaderboard, medals, and daily goal ring — removed as gamification;
  replaced by the private Business Health metrics above
- Checkout-time loyalty point discount — replaced by the rewards catalog

## Known Limitations
- Full-screen "incoming order" alert (like a ride-hailing app) is built but
  only tested for foreground/background app state — not yet verified when
  the app is fully force-closed
- Delivery-related UI does not exist here (deliberately not built — business
  decision)
- No automated tests yet
- `mobile-app/` folder in this repo is unrelated legacy code — do not test
  or reference it
- `DashboardScreen.js` exists in the codebase but is unused/unreferenced —
  don't test it, `SalesDashboardScreen.js` is the real one

## Reporting Bugs
Please include: staff account/role used, exact steps to reproduce,
screenshot if visual, and whether it happens consistently or intermittently.
