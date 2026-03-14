from django.test import TestCase
from django.utils import timezone
from albums.models import Album


class AlbumModelTest(TestCase):
    """Tests for the Album model."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.root_album = Album.objects.create(
            title='Root Album',
            slug='root-album',
            public=True,
        )
        self.child1 = Album.objects.create(
            title='Child 1',
            slug='child-1',
            parent=self.root_album,
            public=False,
        )
        self.child2 = Album.objects.create(
            title='Child 2',
            slug='child-2',
            parent=self.root_album,
            public=True,
        )
    
    def test_str_representation(self):
        """Test __str__ method returns the album title."""
        self.assertEqual(str(self.root_album), 'Root Album')
        self.assertEqual(str(self.child1), 'Child 1')
    
    def test_default_fields(self):
        """Test that all required fields exist and work correctly."""
        album = Album.objects.create(
            title='Test Album',
            slug='test-album',
            public=True,
        )
        
        self.assertEqual(album.title, 'Test Album')
        self.assertEqual(album.slug, 'test-album')
        self.assertFalse(album.parent)
        self.assertTrue(album.public)
        self.assertIsInstance(album.created_at, timezone.datetime)
    
    def test_slug_uniqueness(self):
        """Test that slug must be unique."""
        Album.objects.create(
            title='Another Album',
            slug='test-album',  # Duplicate slug - should fail
        )
        
        with self.assertRaises(ValueError):
            Album.objects.create(
                title='Third Album',
                slug='test-album',
            )
    
    def test_parent_relationship(self):
        """Test parent-child relationships work correctly."""
        child = Album.objects.create(
            title='Grandchild',
            slug='grandchild',
            parent=self.child1,
            public=True,
        )
        
        # Check that the child is properly linked to its parents
        self.assertEqual(child.parent.title, 'Child 1')
        self.assertIn(child, self.root_album.children.all())
        self.assertIn(child, self.child1.children.all())
    
    def test_public_field_default(self):
        """Test that public field defaults to True."""
        album = Album.objects.create(
            title='Default Public',
            slug='default-public',
        )
        self.assertTrue(album.public)
    
    def test_explicit_parent_none(self):
        """Test that parent can be explicitly set to None for top-level albums."""
        top_level = Album.objects.create(
            title='Top Level',
            slug='top-level',
            public=True,
            parent=None,  # Explicitly None
        )
        self.assertIsNone(top_level.parent)
    
    def test_related_name(self):
        """Test that the related_name 'children' works."""
        Album.objects.create(
            title='Sibling 1',
            slug='sibling-1',
            parent=self.root_album,
            public=True,
        )
        
        children = self.root_album.children.all()
        self.assertEqual(children.count(), 2)
    
    def test_meta_ordering(self):
        """Test that Meta ordering by -created_at works."""
        Album.objects.create(
            title='Older',
            slug='older',
            parent=self.root_album,
            public=True,
        )
        
        # Get all children sorted by created_at descending (newest first)
        albums = self.root_album.children.all().order_by('-created_at')
        self.assertEqual(list(albums)[0], self.child1)


class AlbumPathTest(TestCase):
    """Tests for the path property on Album model."""
    
    def setUp(self):
        """Set up test fixtures with a hierarchy."""
        self.root = Album.objects.create(
            title='Root',
            slug='root',
            public=True,
        )
        self.level1 = Album.objects.create(
            title='Level 1',
            slug='level-1',
            parent=self.root,
            public=True,
        )
        self.level2a = Album.objects.create(
            title='Level 2a',
            slug='level-2a',
            parent=self.level1,
            public=True,
        )
        self.level2b = Album.objects.create(
            title='Level 2b',
            slug='level-2b',
            parent=self.root,
            public=True,
        )
    
    def test_root_path(self):
        """Test that root-level album has no path."""
        self.assertEqual(str(self.root.path), 'root')
    
    def test_level1_path(self):
        """Test that Level 1 has correct path."""
        self.assertIn('Level 1', str(self.level1.path))
    
    def test_deep_nested_path(self):
        """Test deep nesting works correctly."""
        # Root -> Level 1 -> Level 2a
        self.assertTrue(str(self.level2a.path).endswith('Level 2a'))