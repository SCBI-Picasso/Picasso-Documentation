add_action( 'get_header', 'remove_titles_all_single_pages' );
function remove_titles_all_single_pages() {
    if ( is_singular('page') ) {
        remove_action( 'genesis_entry_header', 'genesis_do_post_title' );
    }
}