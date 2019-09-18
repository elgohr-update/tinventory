from django.urls import path, include

from ui import views

urlpatterns = [
    path("", views.index, name="ui_index"),
    path("categories/", views.categories, name="ui_categories"),
    path("categories/<int:id>/edit", views.category_edit, name="ui_categories_edit"),
    path("categories/<int:id>/delete", views.category_delete, name="ui_category_delete"),
    path("categories/new", views.category_new, name="ui_category_new"),
    path("locations/", views.locations, name="ui_locations"),
    path("locations/<int:id>/edit", views.location_edit, name="ui_locations_edit"),
    path("locations/<int:id>/delete", views.location_delete, name="ui_location_delete"),
    path("locations/new", views.location_new, name="ui_location_new"),
    path("presets/", views.presets, name="ui_presets"),
    path("presets/<int:id>", views.preset_view, name="ui_presets_view"),
    path("presets/<int:id>/edit", views.preset_edit, name="ui_presets_edit"),
    path("presets/<int:id>/delete", views.preset_delete, name="ui_preset_delete"),
    path("presets/new", views.preset_new, name="ui_preset_new"),
    path("items/", views.items, name="ui_items"),
    path("items/<int:id>", views.item_view, name="ui_items_view"),
    path("items/<int:id>/edit", views.item_edit, name="ui_items_edit"),
    path("items/<int:id>/delete", views.item_delete, name="ui_item_delete"),
    path("items/<int:id>/barcode.pdf", views.item_barcode, name="ui_item_barcode"),
    path("items/new", views.item_new, name="ui_item_new"),
    path("persons/", views.persons, name="ui_persons"),
    path("persons/<int:id>", views.person_view, name="ui_persons_view"),
    path("persons/<int:id>/edit", views.person_edit, name="ui_persons_edit"),
    path("persons/<int:id>/delete", views.person_delete, name="ui_person_delete"),
    path("persons/new", views.person_new, name="ui_person_new"),
    path("inventory/", views.inventory, name="ui_inventory"),
    path("check-out/", views.check_out, name="ui_check_out"),
    path('accounts/', include('django.contrib.auth.urls')),
]
