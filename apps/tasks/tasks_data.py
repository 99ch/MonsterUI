priority_dd = [{'priority': "low", 'count': 36 }, {'priority': "medium", 'count': 33 }, {'priority': "high", 'count': 31 }]

rows_per_page_dd = [10,20,30,40,50]

status_dd = [{'status': "backlog", 'count': 21 },{'status': "todo", 'count': 21 },{'status': "progress", 'count': 20 },{'status': "done",'count': 19 },{'status': "cancelled", 'count': 19 }]

statuses = {
  'backlog': {
    'icon': '''<svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg" class="mr-2 h-4 w-4 text-muted-foreground"><path d="M0.877075 7.49972C0.877075 3.84204 3.84222 0.876892 7.49991 0.876892C11.1576 0.876892 14.1227 3.84204 14.1227 7.49972C14.1227 11.1574 11.1576 14.1226 7.49991 14.1226C3.84222 14.1226 0.877075 11.1574 0.877075 7.49972ZM7.49991 1.82689C4.36689 1.82689 1.82708 4.36671 1.82708 7.49972C1.82708 10.6327 4.36689 13.1726 7.49991 13.1726C10.6329 13.1726 13.1727 10.6327 13.1727 7.49972C13.1727 4.36671 10.6329 1.82689 7.49991 1.82689ZM8.24993 10.5C8.24993 10.9142 7.91414 11.25 7.49993 11.25C7.08571 11.25 6.74993 10.9142 6.74993 10.5C6.74993 10.0858 7.08571 9.75 7.49993 9.75C7.91414 9.75 8.24993 10.0858 8.24993 10.5ZM6.05003 6.25C6.05003 5.57211 6.63511 4.925 7.50003 4.925C8.36496 4.925 8.95003 5.57211 8.95003 6.25C8.95003 6.74118 8.68002 6.99212 8.21447 7.27494C8.16251 7.30651 8.10258 7.34131 8.03847 7.37854L8.03841 7.37858C7.85521 7.48497 7.63788 7.61119 7.47449 7.73849C7.23214 7.92732 6.95003 8.23198 6.95003 8.7C6.95004 9.00376 7.19628 9.25 7.50004 9.25C7.8024 9.25 8.04778 9.00601 8.05002 8.70417L8.05056 8.7033C8.05924 8.6896 8.08493 8.65735 8.15058 8.6062C8.25207 8.52712 8.36508 8.46163 8.51567 8.37436L8.51571 8.37433C8.59422 8.32883 8.68296 8.27741 8.78559 8.21506C9.32004 7.89038 10.05 7.35382 10.05 6.25C10.05 4.92789 8.93511 3.825 7.50003 3.825C6.06496 3.825 4.95003 4.92789 4.95003 6.25C4.95003 6.55376 5.19628 6.8 5.50003 6.8C5.80379 6.8 6.05003 6.55376 6.05003 6.25Z" fill="currentColor" fill-rule="evenodd" clip-rule="evenodd"></path></svg>''',
    'text': "Backlog",
  },
  'cancelled': {
    'icon': '''<svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg" class="mr-2 h-4 w-4 text-muted-foreground"><path d="M0.877075 7.49988C0.877075 3.84219 3.84222 0.877045 7.49991 0.877045C11.1576 0.877045 14.1227 3.84219 14.1227 7.49988C14.1227 11.1575 11.1576 14.1227 7.49991 14.1227C3.84222 14.1227 0.877075 11.1575 0.877075 7.49988ZM7.49991 1.82704C4.36689 1.82704 1.82708 4.36686 1.82708 7.49988C1.82708 10.6329 4.36689 13.1727 7.49991 13.1727C10.6329 13.1727 13.1727 10.6329 13.1727 7.49988C13.1727 4.36686 10.6329 1.82704 7.49991 1.82704ZM9.85358 5.14644C10.0488 5.3417 10.0488 5.65829 9.85358 5.85355L8.20713 7.49999L9.85358 9.14644C10.0488 9.3417 10.0488 9.65829 9.85358 9.85355C9.65832 10.0488 9.34173 10.0488 9.14647 9.85355L7.50002 8.2071L5.85358 9.85355C5.65832 10.0488 5.34173 10.0488 5.14647 9.85355C4.95121 9.65829 4.95121 9.3417 5.14647 9.14644L6.79292 7.49999L5.14647 5.85355C4.95121 5.65829 4.95121 5.3417 5.14647 5.14644C5.34173 4.95118 5.65832 4.95118 5.85358 5.14644L7.50002 6.79289L9.14647 5.14644C9.34173 4.95118 9.65832 4.95118 9.85358 5.14644Z" fill="currentColor" fill-rule="evenodd" clip-rule="evenodd"></path></svg>''',
    'text': "Cancelled",
  },
  'done': {
    'icon': '''<svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg" class="mr-2 h-4 w-4 text-muted-foreground"><path d="M7.49991 0.877045C3.84222 0.877045 0.877075 3.84219 0.877075 7.49988C0.877075 11.1575 3.84222 14.1227 7.49991 14.1227C11.1576 14.1227 14.1227 11.1575 14.1227 7.49988C14.1227 3.84219 11.1576 0.877045 7.49991 0.877045ZM1.82708 7.49988C1.82708 4.36686 4.36689 1.82704 7.49991 1.82704C10.6329 1.82704 13.1727 4.36686 13.1727 7.49988C13.1727 10.6329 10.6329 13.1727 7.49991 13.1727C4.36689 13.1727 1.82708 10.6329 1.82708 7.49988ZM10.1589 5.53774C10.3178 5.31191 10.2636 5.00001 10.0378 4.84109C9.81194 4.68217 9.50004 4.73642 9.34112 4.96225L6.51977 8.97154L5.35681 7.78706C5.16334 7.59002 4.84677 7.58711 4.64973 7.78058C4.45268 7.97404 4.44978 8.29061 4.64325 8.48765L6.22658 10.1003C6.33054 10.2062 6.47617 10.2604 6.62407 10.2483C6.77197 10.2363 6.90686 10.1591 6.99226 10.0377L10.1589 5.53774Z" fill="currentColor" fill-rule="evenodd" clip-rule="evenodd"></path></svg>''',
    'text': "Done",
  },
  'progress': {
    'icon': '''<svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg" class="mr-2 h-4 w-4 text-muted-foreground"><path d="M5.49998 0.5C5.49998 0.223858 5.72383 0 5.99998 0H7.49998H8.99998C9.27612 0 9.49998 0.223858 9.49998 0.5C9.49998 0.776142 9.27612 1 8.99998 1H7.99998V2.11922C9.09832 2.20409 10.119 2.56622 10.992 3.13572C11.0116 3.10851 11.0336 3.08252 11.058 3.05806L11.858 2.25806C12.1021 2.01398 12.4978 2.01398 12.7419 2.25806C12.986 2.50214 12.986 2.89786 12.7419 3.14194L11.967 3.91682C13.1595 5.07925 13.9 6.70314 13.9 8.49998C13.9 12.0346 11.0346 14.9 7.49998 14.9C3.96535 14.9 1.09998 12.0346 1.09998 8.49998C1.09998 5.13362 3.69904 2.3743 6.99998 2.11922V1H5.99998C5.72383 1 5.49998 0.776142 5.49998 0.5ZM2.09998 8.49998C2.09998 5.51764 4.51764 3.09998 7.49998 3.09998C10.4823 3.09998 12.9 5.51764 12.9 8.49998C12.9 11.4823 10.4823 13.9 7.49998 13.9C4.51764 13.9 2.09998 11.4823 2.09998 8.49998ZM7.99998 4.5C7.99998 4.22386 7.77612 4 7.49998 4C7.22383 4 6.99998 4.22386 6.99998 4.5V9.5C6.99998 9.77614 7.22383 10 7.49998 10C7.77612 10 7.99998 9.77614 7.99998 9.5V4.5Z" fill="currentColor" fill-rule="evenodd" clip-rule="evenodd"></path></svg>''',
    'text': "In Progress",
  },
  'todo': {
    'icon': '''<svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg" class="mr-2 h-4 w-4 text-muted-foreground"><path d="M0.877075 7.49991C0.877075 3.84222 3.84222 0.877075 7.49991 0.877075C11.1576 0.877075 14.1227 3.84222 14.1227 7.49991C14.1227 11.1576 11.1576 14.1227 7.49991 14.1227C3.84222 14.1227 0.877075 11.1576 0.877075 7.49991ZM7.49991 1.82708C4.36689 1.82708 1.82708 4.36689 1.82708 7.49991C1.82708 10.6329 4.36689 13.1727 7.49991 13.1727C10.6329 13.1727 13.1727 10.6329 13.1727 7.49991C13.1727 4.36689 10.6329 1.82708 7.49991 1.82708Z" fill="currentColor" fill-rule="evenodd" clip-rule="evenodd"></path></svg>''',
    'text': "Todo",
  },
}

data = [
  {
    "selected": True,
    "id": "TASK-8782",
    "title":
      "You can't compress the program without quantifying the open-source SSD pixel!",
    "status": "progress",
    "label": "documentation",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-7878",
    "title":
      "Try to calculate the EXE feed, maybe it will index the multi-byte pixel!",
    "status": "backlog",
    "label": "documentation",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-7839",
    "title": "We need to bypass the neural TCP card!",
    "status": "todo",
    "label": "bug",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-5562",
    "title":
      "The SAS interface is down, bypass the open-source pixel so we can back up the PNG bandwidth!",
    "status": "backlog",
    "label": "feature",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-8686",
    "title":
      "I'll parse the wireless SSL protocol, that should driver the API panel!",
    "status": "cancelled",
    "label": "feature",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-1280",
    "title":
      "Use the digital TLS panel, then you can transmit the haptic system!",
    "status": "done",
    "label": "bug",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-7262",
    "title":
      "The UTF8 application is down, parse the neural bandwidth so we can back up the PNG firewall!",
    "status": "done",
    "label": "feature",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-1138",
    "title":
      "Generating the driver won't do anything, we need to quantify the 1080p SMTP bandwidth!",
    "status": "progress",
    "label": "feature",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-7184",
    "title": "We need to program the back-end THX pixel!",
    "status": "todo",
    "label": "feature",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-5160",
    "title":
      "Calculating the bus won't do anything, we need to navigate the back-end JSON protocol!",
    "status": "progress",
    "label": "documentation",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-5618",
    "title":
      "Generating the driver won't do anything, we need to index the online SSL application!",
    "status": "done",
    "label": "documentation",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-6699",
    "title":
      "I'll transmit the wireless JBOD capacitor, that should hard drive the SSD feed!",
    "status": "backlog",
    "label": "documentation",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-2858",
    "title": "We need to override the online UDP bus!",
    "status": "backlog",
    "label": "bug",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-9864",
    "title":
      "I'll reboot the 1080p FTP panel, that should matrix the HEX hard drive!",
    "status": "done",
    "label": "bug",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-8404",
    "title": "We need to generate the virtual HEX alarm!",
    "status": "progress",
    "label": "bug",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-5365",
    "title":
      "Backing up the pixel won't do anything, we need to transmit the primary IB array!",
    "status": "progress",
    "label": "documentation",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-1780",
    "title":
      "The CSS feed is down, index the bluetooth transmitter so we can compress the CLI protocol!",
    "status": "todo",
    "label": "documentation",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-6938",
    "title":
      "Use the redundant SCSI application, then you can hack the optical alarm!",
    "status": "todo",
    "label": "documentation",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-9885",
    "title": "We need to compress the auxiliary VGA driver!",
    "status": "backlog",
    "label": "bug",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-3216",
    "title":
      "Transmitting the transmitter won't do anything, we need to compress the virtual HDD sensor!",
    "status": "backlog",
    "label": "documentation",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-9285",
    "title":
      "The IP monitor is down, copy the haptic alarm so we can generate the HTTP transmitter!",
    "status": "todo",
    "label": "bug",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-1024",
    "title":
      "Overriding the microchip won't do anything, we need to transmit the digital OCR transmitter!",
    "status": "progress",
    "label": "documentation",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-7068",
    "title":
      "You can't generate the capacitor without indexing the wireless HEX pixel!",
    "status": "cancelled",
    "label": "bug",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-6502",
    "title":
      "Navigating the microchip won't do anything, we need to bypass the back-end SQL bus!",
    "status": "todo",
    "label": "bug",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-5326",
    "title": "We need to hack the redundant UTF8 transmitter!",
    "status": "todo",
    "label": "bug",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-6274",
    "title":
      "Use the virtual PCI circuit, then you can parse the bluetooth alarm!",
    "status": "cancelled",
    "label": "documentation",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-1571",
    "title":
      "I'll input the neural DRAM circuit, that should protocol the SMTP interface!",
    "status": "progress",
    "label": "feature",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-9518",
    "title":
      "Compressing the interface won't do anything, we need to compress the online SDD matrix!",
    "status": "cancelled",
    "label": "documentation",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-5581",
    "title":
      "I'll synthesize the digital COM pixel, that should transmitter the UTF8 protocol!",
    "status": "backlog",
    "label": "documentation",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-2197",
    "title":
      "Parsing the feed won't do anything, we need to copy the bluetooth DRAM bus!",
    "status": "todo",
    "label": "documentation",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-8484",
    "title": "We need to parse the solid state UDP firewall!",
    "status": "progress",
    "label": "bug",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-9892",
    "title":
      "If we back up the application, we can get to the UDP application through the multi-byte THX capacitor!",
    "status": "done",
    "label": "documentation",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-9616",
    "title": "We need to synthesize the cross-platform ASCII pixel!",
    "status": "progress",
    "label": "feature",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-9744",
    "title":
      "Use the back-end IP card, then you can input the solid state hard drive!",
    "status": "done",
    "label": "documentation",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-1376",
    "title":
      "Generating the alarm won't do anything, we need to generate the mobile IP capacitor!",
    "status": "backlog",
    "label": "documentation",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-7382",
    "title":
      "If we back up the firewall, we can get to the RAM alarm through the primary UTF8 pixel!",
    "status": "todo",
    "label": "feature",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-2290",
    "title":
      "I'll compress the virtual JSON panel, that should application the UTF8 bus!",
    "status": "cancelled",
    "label": "documentation",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-1533",
    "title":
      "You can't input the firewall without overriding the wireless TCP firewall!",
    "status": "done",
    "label": "bug",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-4920",
    "title":
      "Bypassing the hard drive won't do anything, we need to input the bluetooth JSON program!",
    "status": "progress",
    "label": "bug",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-5168",
    "title":
      "If we synthesize the bus, we can get to the IP panel through the virtual TLS array!",
    "status": "progress",
    "label": "feature",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-7103",
    "title": "We need to parse the multi-byte EXE bandwidth!",
    "status": "cancelled",
    "label": "feature",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-4314",
    "title":
      "If we compress the program, we can get to the XML alarm through the multi-byte COM matrix!",
    "status": "progress",
    "label": "bug",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-3415",
    "title":
      "Use the cross-platform XML application, then you can quantify the solid state feed!",
    "status": "todo",
    "label": "feature",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-8339",
    "title":
      "Try to calculate the DNS interface, maybe it will input the bluetooth capacitor!",
    "status": "progress",
    "label": "feature",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-6995",
    "title":
      "Try to hack the XSS bandwidth, maybe it will override the bluetooth matrix!",
    "status": "todo",
    "label": "feature",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-8053",
    "title":
      "If we connect the program, we can get to the UTF8 matrix through the digital UDP protocol!",
    "status": "todo",
    "label": "feature",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-4336",
    "title":
      "If we synthesize the microchip, we can get to the SAS sensor through the optical UDP program!",
    "status": "todo",
    "label": "documentation",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-8790",
    "title":
      "I'll back up the optical COM alarm, that should alarm the RSS capacitor!",
    "status": "done",
    "label": "bug",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-8980",
    "title":
      "Try to navigate the SQL transmitter, maybe it will back up the virtual firewall!",
    "status": "cancelled",
    "label": "bug",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-7342",
    "title": "Use the neural CLI card, then you can parse the online port!",
    "status": "backlog",
    "label": "documentation",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-5608",
    "title":
      "I'll hack the haptic SSL program, that should bus the UDP transmitter!",
    "status": "cancelled",
    "label": "documentation",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-1606",
    "title":
      "I'll generate the bluetooth PNG firewall, that should pixel the SSL driver!",
    "status": "done",
    "label": "feature",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-7872",
    "title":
      "Transmitting the circuit won't do anything, we need to reboot the 1080p RSS monitor!",
    "status": "cancelled",
    "label": "feature",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-4167",
    "title":
      "Use the cross-platform SMS circuit, then you can synthesize the optical feed!",
    "status": "cancelled",
    "label": "bug",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-9581",
    "title":
      "You can't index the port without hacking the cross-platform XSS monitor!",
    "status": "backlog",
    "label": "documentation",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-8806",
    "title": "We need to bypass the back-end SSL panel!",
    "status": "done",
    "label": "bug",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-6542",
    "title":
      "Try to quantify the RSS firewall, maybe it will quantify the open-source system!",
    "status": "done",
    "label": "feature",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-6806",
    "title":
      "The VGA protocol is down, reboot the back-end matrix so we can parse the CSS panel!",
    "status": "cancelled",
    "label": "documentation",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-9549",
    "title": "You can't bypass the bus without connecting the neural JBOD bus!",
    "status": "todo",
    "label": "feature",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-1075",
    "title":
      "Backing up the driver won't do anything, we need to parse the redundant RAM pixel!",
    "status": "done",
    "label": "feature",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-1427",
    "title":
      "Use the auxiliary PCI circuit, then you can calculate the cross-platform interface!",
    "status": "done",
    "label": "documentation",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-1907",
    "title":
      "Hacking the circuit won't do anything, we need to back up the online DRAM system!",
    "status": "todo",
    "label": "documentation",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-4309",
    "title":
      "If we generate the system, we can get to the TCP sensor through the optical GB pixel!",
    "status": "backlog",
    "label": "bug",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-3973",
    "title":
      "I'll parse the back-end ADP array, that should bandwidth the RSS bandwidth!",
    "status": "todo",
    "label": "feature",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-7962",
    "title":
      "Use the wireless RAM program, then you can hack the cross-platform feed!",
    "status": "cancelled",
    "label": "bug",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-3360",
    "title":
      "You can't quantify the program without synthesizing the neural OCR interface!",
    "status": "done",
    "label": "feature",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-9887",
    "title":
      "Use the auxiliary ASCII sensor, then you can connect the solid state port!",
    "status": "backlog",
    "label": "bug",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-3649",
    "title":
      "I'll input the virtual USB system, that should circuit the DNS monitor!",
    "status": "progress",
    "label": "feature",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-3586",
    "title":
      "If we quantify the circuit, we can get to the CLI feed through the mobile SMS hard drive!",
    "status": "progress",
    "label": "bug",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-5150",
    "title":
      "I'll hack the wireless XSS port, that should transmitter the IP interface!",
    "status": "cancelled",
    "label": "feature",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-3652",
    "title":
      "The SQL interface is down, override the optical bus so we can program the ASCII interface!",
    "status": "backlog",
    "label": "feature",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-6884",
    "title":
      "Use the digital PCI circuit, then you can synthesize the multi-byte microchip!",
    "status": "cancelled",
    "label": "feature",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-1591",
    "title": "We need to connect the mobile XSS driver!",
    "status": "progress",
    "label": "feature",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-3802",
    "title":
      "Try to override the ASCII protocol, maybe it will parse the virtual matrix!",
    "status": "progress",
    "label": "feature",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-7253",
    "title":
      "Programming the capacitor won't do anything, we need to bypass the neural IB hard drive!",
    "status": "backlog",
    "label": "bug",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-9739",
    "title": "We need to hack the multi-byte HDD bus!",
    "status": "done",
    "label": "documentation",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-4424",
    "title":
      "Try to hack the HEX alarm, maybe it will connect the optical pixel!",
    "status": "progress",
    "label": "documentation",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-3922",
    "title":
      "You can't back up the capacitor without generating the wireless PCI program!",
    "status": "backlog",
    "label": "bug",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-4921",
    "title":
      "I'll index the open-source IP feed, that should system the GB application!",
    "status": "cancelled",
    "label": "bug",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-5814",
    "title": "We need to calculate the 1080p AGP feed!",
    "status": "backlog",
    "label": "bug",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-2645",
    "title":
      "Synthesizing the system won't do anything, we need to navigate the multi-byte HDD firewall!",
    "status": "todo",
    "label": "documentation",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-4535",
    "title":
      "Try to copy the JSON circuit, maybe it will connect the wireless feed!",
    "status": "progress",
    "label": "feature",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-4463",
    "title": "We need to copy the solid state AGP monitor!",
    "status": "done",
    "label": "documentation",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-9745",
    "title":
      "If we connect the protocol, we can get to the GB system through the bluetooth PCI microchip!",
    "status": "cancelled",
    "label": "feature",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-2080",
    "title":
      "If we input the bus, we can get to the RAM matrix through the auxiliary RAM card!",
    "status": "todo",
    "label": "bug",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-3838",
    "title":
      "I'll bypass the online TCP application, that should panel the AGP system!",
    "status": "backlog",
    "label": "bug",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-1340",
    "title": "We need to navigate the virtual PNG circuit!",
    "status": "todo",
    "label": "bug",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-6665",
    "title":
      "If we parse the monitor, we can get to the SSD hard drive through the cross-platform AGP alarm!",
    "status": "cancelled",
    "label": "feature",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-7585",
    "title":
      "If we calculate the hard drive, we can get to the SSL program through the multi-byte CSS microchip!",
    "status": "backlog",
    "label": "feature",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-6319",
    "title": "We need to copy the multi-byte SCSI program!",
    "status": "backlog",
    "label": "bug",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-4369",
    "title": "Try to input the SCSI bus, maybe it will generate the 1080p pixel!",
    "status": "backlog",
    "label": "bug",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-9035",
    "title": "We need to override the solid state PNG array!",
    "status": "cancelled",
    "label": "documentation",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-3970",
    "title":
      "You can't index the transmitter without quantifying the haptic ASCII card!",
    "status": "todo",
    "label": "documentation",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-4473",
    "title":
      "You can't bypass the protocol without overriding the neural RSS program!",
    "status": "todo",
    "label": "documentation",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-4136",
    "title":
      "You can't hack the hard drive without hacking the primary JSON program!",
    "status": "cancelled",
    "label": "bug",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-3939",
    "title":
      "Use the back-end SQL firewall, then you can connect the neural hard drive!",
    "status": "done",
    "label": "feature",
    "priority": "low",
  },
  {
    "selected": False,
    "id": "TASK-2007",
    "title":
      "I'll input the back-end USB protocol, that should bandwidth the PCI system!",
    "status": "backlog",
    "label": "bug",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-7516",
    "title":
      "Use the primary SQL program, then you can generate the auxiliary transmitter!",
    "status": "done",
    "label": "documentation",
    "priority": "medium",
  },
  {
    "selected": False,
    "id": "TASK-6906",
    "title":
      "Try to back up the DRAM system, maybe it will reboot the online transmitter!",
    "status": "done",
    "label": "feature",
    "priority": "high",
  },
  {
    "selected": False,
    "id": "TASK-5207",
    "title":
      "The SMS interface is down, copy the bluetooth bus so we can quantify the VGA card!",
    "status": "progress",
    "label": "bug",
    "priority": "low",
  },
]
