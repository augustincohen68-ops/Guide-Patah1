import flet as ft

def main(page: ft.Page):
    page.title = "Mon Guide Patah' Eliahou"
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Force la page principale à tout aligner au centre
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Textes d'affichage du haut
    result_title = ft.Text("Sélectionnez une catégorie", size=16, weight=ft.FontWeight.BOLD, color="#102A43", text_align=ft.TextAlign.CENTER)
    result_page = ft.Text("Page --", size=32, weight=ft.FontWeight.BOLD, color="#D4AF37", text_align=ft.TextAlign.CENTER)
    result_precision = ft.Text("Choisissez un thème ci-dessous.", size=13, color="#102A43", text_align=ft.TextAlign.CENTER)
    
    # Panneau du haut centré
    display_panel = ft.Container(
        content=ft.Column(
            [result_title, result_page, result_precision],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        bgcolor="#E2E8F0",
        padding=20,
        border_radius=10,
        width=340
    )

    # Zone de contenu centrée
    content_area = ft.Column(
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    def update_display(name, page_num, precision):
        result_title.value = name.upper()
        result_page.value = f"Page {page_num}" if page_num != "--" else "Page --"
        result_precision.value = f"💡 {precision}" if precision else ""
        page.update()

    def create_back_button():
        return ft.ElevatedButton(
            "⬅ Retour au Menu Principal", 
            on_click=lambda e: show_main_menu(),
            width=340
        )

    def make_row_item(name, page_num, precision):
        return ft.Container(
            content=ft.Row([
                ft.Text(f" {name}", size=14, expand=True),
                ft.Text(f"p. {page_num} " if page_num != "--" else "", size=14, weight=ft.FontWeight.BOLD)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            bgcolor="white",
            padding=15,
            border_radius=8,
            width=340,
            on_click=lambda e: update_display(name, page_num, precision)
        )

    def show_shabbat():
        content_area.controls.clear()
        content_area.controls.append(create_back_button())
        shabbat_data = [
            ("Allumage des bougies", "--", "Juste avant l'heure du Shabbat, vous commencez par là."),
            ("Kabbalat Shabbat", "152", "Psaumes et Lekha Dodi (p.166). Moment très joyeux."),
            ("'Arbith", "169", "Chema et Amida debout face à l'Est. Sautez le Kaddiche."),
            ("Le repas", "189", "Kiddouche à table sur le vin."),
            ("Cha'hrith", "190", "Louanges du matin (Pesoukei Dezimra)."),
            ("Le Chema", "212", "Réciter le Chema. Sautez le Barekhou au début."),
            ("La 'Amida du matin", "221", "Debout à voix basse. Pas de Kedoucha."),
            ("Moussaf", "237", "Office supplémentaire directement après la 'Amida."),
            ("Le repas du midi", "251", "Kiddouche du matin avant le repas chaud.")
        ]
        for name, p, pr in shabbat_data:
            content_area.controls.append(make_row_item(name, p, pr))
        page.update()

    def show_semaine():
        content_area.controls.clear()
        content_area.controls.append(create_back_button())
        semaine_data = [
            ("Bénédictions du matin", "1", "Prières dès le réveil pour remercier Dieu."),
            ("Mise du Tallith", "5", "S'envelopper du châle de prière à franges."),
            ("Pose des Tefilline", "6", "Attacher les phylactères (semaine uniquement)."),
            ("« Pata'h Eliahou »", "9", "Discours mystique du Zohar très cher au rite séfarade."),
            ("☀️ CHA'HRITH (Matin)", "19", "Office principal du matin avec le Chema et l'Amida."),
            ("⛅ MIN'HA (Après-midi)", "108", "Office court avant le coucher du soleil."),
            ("🌙 'ARBITH (Soir)", "131", "Office de la nuit.")
        ]
        for name, p, pr in semaine_data:
            content_area.controls.append(make_row_item(name, p, pr))
        page.update()

    def show_fetes():
        content_area.controls.clear()
        content_area.controls.append(create_back_button())
        fetes_data = [
            ("ROCHE 'HODECHE", "294", "Nouveau mois juif. Ajout de 'Yaalé Veyavo'."),
            (" - Hallel", "294", "Psaumes de louanges (113 à 118) chantés."),
            (" - Moussaf Roch 'Hodech", "305", "Office additionnel du début de mois."),
            ("Hanoucca", "315", "Allumage et insertion de 'Al HaNissim'."),
            ("Prières des Trois-Fêtes", "332", "Amida pour Pessa'h, Chavouot et Souccot."),
            ("Supputation de l'« Omère »", "352", "Décompte des 49 jours à la tombée de la nuit.")
        ]
        for name, p, pr in fetes_data:
            content_area.controls.append(make_row_item(name, p, pr))
        page.update()

    def show_benedictions():
        content_area.controls.clear()
        content_area.controls.append(create_back_button())
        bénéd_data = [
            ("Bénédictions avant le repas", "374", "Selon la nature de l'aliment."),
            ("Actions de grâces (Repas)", "375", "Le Birkat Hamazone après le pain."),
            ("Prière du voyage", "387", "Tefilat Haderekh pour la protection sur la route."),
            ("Prière du coucher", "389", "Chema du coucher pour confier son âme."),
            ("Prière pour les malades", "392", "Le Mishébérakh pour la guérison.")
        ]
        for name, p, pr in bénéd_data:
            content_area.controls.append(make_row_item(name, p, pr))
        page.update()

    def show_main_menu():
        content_area.controls.clear()
        result_title.value = "Sélectionnez une catégorie"
        result_page.value = "Page --"
        result_precision.value = "Choisissez un thème ci-dessous."
        
        menu_items = [
            ("🕯️ SHABBAT", show_shabbat),
            ("📅 SEMAINE", show_semaine),
            ("🌙 ROCH H'ODECH & FÊTES", show_fetes),
            ("🍽️ BÉNÉDICTIONS", show_benedictions)
        ]
        
        for text, action in menu_items:
            content_area.controls.append(
                ft.ElevatedButton(text, on_click=lambda e, a=action: a(), width=340)
            )
        page.update()

    # Changement ici : height=100 pour descendre encore plus l'application
    main_layout = ft.Column(
        [
            ft.Container(height=100), 
            ft.Text("Guide Patah' Eliahou", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            display_panel,
            content_area
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=340
    )

    page.add(main_layout)
    show_main_menu()

ft.app(target=main)