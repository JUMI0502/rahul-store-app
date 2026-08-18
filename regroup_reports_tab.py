with open('screens/MainStore.js', 'r') as f:
    content = f.read()

changes = 0

old = '''            {/* STAFF MANAGER */}
            {isOwner && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => { fetchAllStaff(); setShowStaffManager(true); }}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="people-circle" size={22} color="#C9A84C" />
                  <View>
                    <Text style={s.customerHistoryBtnTitle}>Staff Manager</Text>
                    <Text style={s.customerHistoryBtnSub}>Add, view and manage staff profiles</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {/* ABANDONED CARTS */}
            {(isOwner || isSenior) && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => setShowAbandonedCarts(true)}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="cart" size={22} color="#4F6EF7" />
                  <View>
                    <Text style={s.customerHistoryBtnTitle}>Abandoned Carts</Text>
                    <Text style={s.customerHistoryBtnSub}>Nudge customers who didn't finish checking out</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {/* WARRANTY & RETURNS */}
            {(isOwner || isSenior) && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => setShowWarrantyReturns(true)}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="shield-checkmark" size={22} color="#F59E0B" />
                  <View>
                    <Text style={s.customerHistoryBtnTitle}>Warranty & Returns</Text>
                    <Text style={s.customerHistoryBtnSub}>Track defect claims and resolutions</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {/* SERVICE REMINDERS */}
            {(isOwner || isSenior) && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => setShowServiceReminders(true)}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="time" size={22} color="#25D366" />
                  <View>
                    <Text style={s.customerHistoryBtnTitle}>Service Reminders</Text>
                    <Text style={s.customerHistoryBtnSub}>Nudge customers who haven't visited recently</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {/* MECHANIC APPROVALS */}
            {(isOwner || isSenior) && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => { fetchMechanics(); setShowMechanicApprovals(true); }}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="construct" size={22} color="#F59E0B" />
                  <View>
                    <Text style={s.customerHistoryBtnTitle}>Mechanic Approvals</Text>
                    <Text style={s.customerHistoryBtnSub}>
                      {mechanicsPendingCount > 0 ? `${mechanicsPendingCount} pending request(s)` : 'Review mechanic access requests'}
                    </Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {/* ACTIVITY LOG */}
            {isOwner && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => { fetchActivityLog(); setShowActivityLog(true); }}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="list-circle" size={22} color="#4F6EF7" />
                  <View>
                    <Text style={s.customerHistoryBtnTitle}>Activity Log</Text>
                    <Text style={s.customerHistoryBtnSub}>See all staff actions in real-time</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {/* BULK WHATSAPP */}
            {isOwner && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => setShowBulkMessage(true)}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="megaphone" size={22} color="#25D366" />
                  <View>
                    <Text style={s.customerHistoryBtnTitle}>Bulk WhatsApp</Text>
                    <Text style={s.customerHistoryBtnSub}>Send message to all customers</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {/* END OF DAY */}
            {isOwner && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => setShowEndOfDay(true)}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="moon" size={22} color="#8B5CF6" />
                  <View>
                    <Text style={s.customerHistoryBtnTitle}>End of Day Report</Text>
                    <Text style={s.customerHistoryBtnSub}>Daily summary to owner WhatsApp</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {/* STOCK ADJUSTMENT */}
            {isOwner && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => { fetchProducts(); setShowStockAdjust(true); }}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="settings" size={22} color="#F59E0B" />
                  <View>
                    <Text style={s.customerHistoryBtnTitle}>Stock Adjustment</Text>
                    <Text style={s.customerHistoryBtnSub}>Write-off, damage, physical count</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {/* CUSTOMER BLACKLIST */}
            {isOwner && (
              <TouchableOpacity style={[s.customerHistoryBtn, { borderColor: 'rgba(239,68,68,0.2)' }]}
                onPress={() => setShowBlacklist(true)}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="ban" size={22} color="#EF4444" />
                  <View>
                    <Text style={[s.customerHistoryBtnTitle, { color: '#EF4444' }]}>Customer Blacklist</Text>
                    <Text style={s.customerHistoryBtnSub}>Block problematic customers</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {/* REWARDS MANAGER */}
            {isOwner && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => setShowRewardManager(true)}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="gift" size={22} color="#C9A84C" />
                  <View>
                    <Text style={[s.customerHistoryBtnTitle, { color: '#C9A84C' }]}>Rewards Manager</Text>
                    <Text style={s.customerHistoryBtnSub}>Set free products for point redemption</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {/* CUSTOMER HISTORY BUTTON */}
            <TouchableOpacity style={s.customerHistoryBtn}
              onPress={() => { fetchAllCustomers(); setShowCustomerHistory(true); }}>
              <View style={s.customerHistoryBtnLeft}>
                <Ionicons name="people" size={22} color="#4F6EF7" />
                <View>
                  <Text style={s.customerHistoryBtnTitle}>Customer History</Text>
                  <Text style={s.customerHistoryBtnSub}>View all customer orders</Text>
                </View>
              </View>
              <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
            </TouchableOpacity>'''

new = '''            {/* ═══ CUSTOMER TOOLS ═══ */}
            <Text style={s.reportsSectionLabel}>CUSTOMER TOOLS</Text>

            <TouchableOpacity style={s.customerHistoryBtn}
              onPress={() => { fetchAllCustomers(); setShowCustomerHistory(true); }}>
              <View style={s.customerHistoryBtnLeft}>
                <Ionicons name="people" size={22} color="#4F6EF7" />
                <View>
                  <Text style={s.customerHistoryBtnTitle}>Customer History</Text>
                  <Text style={s.customerHistoryBtnSub}>View all customer orders</Text>
                </View>
              </View>
              <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
            </TouchableOpacity>

            {(isOwner || isSenior) && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => setShowAbandonedCarts(true)}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="cart" size={22} color="#4F6EF7" />
                  <View>
                    <Text style={s.customerHistoryBtnTitle}>Abandoned Carts</Text>
                    <Text style={s.customerHistoryBtnSub}>Nudge customers who didn't finish checking out</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {(isOwner || isSenior) && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => setShowServiceReminders(true)}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="time" size={22} color="#25D366" />
                  <View>
                    <Text style={s.customerHistoryBtnTitle}>Service Reminders</Text>
                    <Text style={s.customerHistoryBtnSub}>Nudge customers who haven't visited recently</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {isOwner && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => setShowBulkMessage(true)}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="megaphone" size={22} color="#25D366" />
                  <View>
                    <Text style={s.customerHistoryBtnTitle}>Bulk WhatsApp</Text>
                    <Text style={s.customerHistoryBtnSub}>Send message to all customers</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {isOwner && (
              <TouchableOpacity style={[s.customerHistoryBtn, { borderColor: 'rgba(239,68,68,0.2)' }]}
                onPress={() => setShowBlacklist(true)}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="ban" size={22} color="#EF4444" />
                  <View>
                    <Text style={[s.customerHistoryBtnTitle, { color: '#EF4444' }]}>Customer Blacklist</Text>
                    <Text style={s.customerHistoryBtnSub}>Block problematic customers</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {isOwner && (
              <>
                <Text style={s.reportsSectionLabel}>INVENTORY & OPERATIONS</Text>
                <TouchableOpacity style={s.customerHistoryBtn}
                  onPress={() => { fetchProducts(); setShowStockAdjust(true); }}>
                  <View style={s.customerHistoryBtnLeft}>
                    <Ionicons name="settings" size={22} color="#F59E0B" />
                    <View>
                      <Text style={s.customerHistoryBtnTitle}>Stock Adjustment</Text>
                      <Text style={s.customerHistoryBtnSub}>Write-off, damage, physical count</Text>
                    </View>
                  </View>
                  <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
                </TouchableOpacity>
              </>
            )}

            {(isOwner || isSenior) && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => setShowWarrantyReturns(true)}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="shield-checkmark" size={22} color="#F59E0B" />
                  <View>
                    <Text style={s.customerHistoryBtnTitle}>Warranty & Returns</Text>
                    <Text style={s.customerHistoryBtnSub}>Track defect claims and resolutions</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {isOwner && (
              <TouchableOpacity style={s.customerHistoryBtn}
                onPress={() => setShowRewardManager(true)}>
                <View style={s.customerHistoryBtnLeft}>
                  <Ionicons name="gift" size={22} color="#C9A84C" />
                  <View>
                    <Text style={[s.customerHistoryBtnTitle, { color: '#C9A84C' }]}>Rewards Manager</Text>
                    <Text style={s.customerHistoryBtnSub}>Set free products for point redemption</Text>
                  </View>
                </View>
                <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
              </TouchableOpacity>
            )}

            {(isOwner || isSenior) && (
              <>
                <Text style={s.reportsSectionLabel}>APPROVALS</Text>
                <TouchableOpacity style={s.customerHistoryBtn}
                  onPress={() => { fetchMechanics(); setShowMechanicApprovals(true); }}>
                  <View style={s.customerHistoryBtnLeft}>
                    <Ionicons name="construct" size={22} color="#F59E0B" />
                    <View>
                      <Text style={s.customerHistoryBtnTitle}>Mechanic Approvals</Text>
                      <Text style={s.customerHistoryBtnSub}>
                        {mechanicsPendingCount > 0 ? `${mechanicsPendingCount} pending request(s)` : 'Review mechanic access requests'}
                      </Text>
                    </View>
                  </View>
                  <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
                </TouchableOpacity>
              </>
            )}

            {isOwner && (
              <>
                <Text style={s.reportsSectionLabel}>BUSINESS & STAFF</Text>
                <TouchableOpacity style={s.customerHistoryBtn}
                  onPress={() => { fetchAllStaff(); setShowStaffManager(true); }}>
                  <View style={s.customerHistoryBtnLeft}>
                    <Ionicons name="people-circle" size={22} color="#C9A84C" />
                    <View>
                      <Text style={s.customerHistoryBtnTitle}>Staff Manager</Text>
                      <Text style={s.customerHistoryBtnSub}>Add, view and manage staff profiles</Text>
                    </View>
                  </View>
                  <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
                </TouchableOpacity>

                <TouchableOpacity style={s.customerHistoryBtn}
                  onPress={() => { fetchActivityLog(); setShowActivityLog(true); }}>
                  <View style={s.customerHistoryBtnLeft}>
                    <Ionicons name="list-circle" size={22} color="#4F6EF7" />
                    <View>
                      <Text style={s.customerHistoryBtnTitle}>Activity Log</Text>
                      <Text style={s.customerHistoryBtnSub}>See all staff actions in real-time</Text>
                    </View>
                  </View>
                  <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
                </TouchableOpacity>

                <TouchableOpacity style={s.customerHistoryBtn}
                  onPress={() => setShowEndOfDay(true)}>
                  <View style={s.customerHistoryBtnLeft}>
                    <Ionicons name="moon" size={22} color="#8B5CF6" />
                    <View>
                      <Text style={s.customerHistoryBtnTitle}>End of Day Report</Text>
                      <Text style={s.customerHistoryBtnSub}>Daily summary to owner WhatsApp</Text>
                    </View>
                  </View>
                  <Ionicons name="chevron-forward" size={18} color="rgba(255,255,255,0.3)" />
                </TouchableOpacity>
              </>
            )}'''

if old in content:
    content = content.replace(old, new, 1)
    changes += 1
    print("1/2: all 12 items regrouped into 4 labeled sections")
else:
    print("FAILED 1/2 - anchor not found")

old_style = "  customerHistoryBtn: {"
new_style = '''  reportsSectionLabel: {
    fontSize: 11, color: 'rgba(201,168,76,0.5)', fontWeight: '700',
    letterSpacing: 1.5, marginTop: 14, marginBottom: 8,
  },
  customerHistoryBtn: {'''
if old_style in content:
    content = content.replace(old_style, new_style, 1)
    changes += 1
    print("2/2: reportsSectionLabel style added")
else:
    print("FAILED 2/2 - style anchor not found")

with open('screens/MainStore.js', 'w') as f:
    f.write(content)

print(f"\n{changes}/2 applied")
