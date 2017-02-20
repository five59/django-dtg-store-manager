Publishing a Batch of New Products
==================================


*WARNING* THIS DOCUMENTATION IS OUT OF DATE.

To process a batch of incoming products from Printful to WooCommerce:


1. Create the Products in The Printful, but leave unpublished.

2. Launch the iPython shell with ""./manage.sh shell_plus"

3. Run the following code (replacing  your shop code with the appropriate code). It will download all of your products from your WooCommerce shop.

   >>> from outlet_woo import interface as wi
   >>> a = wi.APIInterface(Shop.objects.get(code='BG'))
   >>> a.do_import()

4. Go to the WooCommerce>Product menu, and update the links for your new products to the Product and Design objects.

5. Go to the WooCommerce>Product Variations menu, and update the links for your new products to the Color and Size objects. You can do a rough-match with the following (swapping out your Brand and Product codes):

   >>> for pv in ProductVariation.objects.filter(product__item__code='4041', product__item__brand__code='AA'):
   ...     pv.update_meta()
   ...     pv.save()

6. Almost there... now update the attributes and descriptions. This is done off of the outlet_woo.Product object:

   >>> for p in wm.Product.objects.filter(item__code='4041', item__brand__code='AA'):
   ...     p.update_attributes()
   ...     p.update_description()

7. Now you're ready to push your data (provided you didn't destroy the 'a' variable holding your API Instance):

   >>> a.push_data()

8. All that's left is to set "Published" on your new products on the site.
