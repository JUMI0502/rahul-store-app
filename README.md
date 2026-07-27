# New Rahul Auto Spares — Store App

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
feature) and cannot run in Expo Go.
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
- Order lifecycle: New → Packing → Ready → Collected, confirm status updates
  instantly and syncs correctly in the order detail view
- Push notification: place a test order from the customer app, confirm "New
  Order!" arrives even with this app closed
- Staff Manager (owner/senior only): Add, Edit, Delete, Reset PIN
- Mechanic Approvals (owner/senior only): approve/reject a pending mechanic
  registration submitted from the customer app
- Stock: adjust quantity, mark items OEM vs Generic/Compatible from the
  Stock tab
- Scanner tab: scan a customer's order QR code, confirm it offers "Mark as
  Collected"
- Clock In / Clock Out (Attendance)

## Known Limitations
- Full-screen "incoming order" alert (like a ride-hailing app) is built but
  only tested for foreground/background app state — not yet verified when
  the app is fully force-closed
- No automated tests yet
- `mobile-app/` folder in this repo is unrelated legacy code — do not test
  or reference it

## Reporting Bugs
Please include: staff account/role used, exact steps to reproduce,
screenshot if visual, and whether it happens consistently or intermittently.
