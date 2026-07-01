import { useState, useEffect } from 'react';
import './App.css';

const API_BASE_URL = 'http://localhost:8000';

function App() {
  const [products, setProducts] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  // Form State
  const [formData, setFormData] = useState({
    id: '',
    name: '',
    description: '',
    price: '',
    quantity: ''
  });
  const [isEditing, setIsEditing] = useState(false);

  // Search and Sort State
  const [searchQuery, setSearchQuery] = useState('');
  const [sortField, setSortField] = useState('id');
  const [sortOrder, setSortOrder] = useState('asc'); // 'asc' or 'desc'

  // Fetch all products
  const fetchProducts = async () => {
    try {
      setIsLoading(true);
      const response = await fetch(`${API_BASE_URL}/products`);
      if (!response.ok) {
        throw new Error('Could not fetch products from database');
      }
      const data = await response.json();
      setProducts(data);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  // Form inputs change handler
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value
    }));
  };

  // Submit Handler (Add or Update)
  const handleSubmit = async (e) => {
    e.preventDefault();
    const endpoint = isEditing ? `${API_BASE_URL}/product/${formData.id}` : `${API_BASE_URL}/product`;
    const method = isEditing ? 'PUT' : 'POST';

    try {
      const response = await fetch(endpoint, {
        method: method,
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          id: parseInt(formData.id),
          name: formData.name,
          description: formData.description,
          price: parseFloat(formData.price),
          quantity: parseInt(formData.quantity)
        })
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || data.error || 'Failed to save product');
      }

      // Reset form and mode
      setFormData({ id: '', name: '', description: '', price: '', quantity: '' });
      setIsEditing(false);
      setError(null);
      fetchProducts();
    } catch (err) {
      setError(err.message);
    }
  };

  // Click Edit handler
  const handleEditClick = (product) => {
    setIsEditing(true);
    setFormData({
      id: product.id.toString(),
      name: product.name,
      description: product.description,
      price: product.price.toString(),
      quantity: product.quantity.toString()
    });
  };

  // Cancel edit handler
  const handleCancelEdit = () => {
    setIsEditing(false);
    setFormData({ id: '', name: '', description: '', price: '', quantity: '' });
  };

  // Delete product handler
  const handleDeleteClick = async (id) => {
    if (!window.confirm(`Are you sure you want to delete product with ID ${id}?`)) {
      return;
    }

    try {
      const response = await fetch(`${API_BASE_URL}/product/${id}`, {
        method: 'DELETE'
      });

      if (!response.ok) {
        throw new Error('Failed to delete product');
      }

      fetchProducts();
    } catch (err) {
      setError(err.message);
    }
  };

  // Toggle sorting
  const handleSort = (field) => {
    if (sortField === field) {
      setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc');
    } else {
      setSortField(field);
      setSortOrder('asc');
    }
  };

  // Filter products by search query
  const filteredProducts = products.filter((product) => {
    const query = searchQuery.toLowerCase();
    return (
      product.id.toString().includes(query) ||
      product.name.toLowerCase().includes(query) ||
      product.description.toLowerCase().includes(query)
    );
  });

  // Sort filtered products
  const sortedProducts = [...filteredProducts].sort((a, b) => {
    let valA = a[sortField];
    let valB = b[sortField];

    if (typeof valA === 'string') {
      valA = valA.toLowerCase();
      valB = valB.toLowerCase();
    }

    if (valA < valB) return sortOrder === 'asc' ? -1 : 1;
    if (valA > valB) return sortOrder === 'asc' ? 1 : -1;
    return 0;
  });

  return (
    <div className="app-container">
      {/* Header Row */}
      <header className="app-header">
        <div className="total-badge">
          Total: {products.length}
        </div>
        <div className="search-container">
          <span className="search-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
              <circle cx="11" cy="11" r="8"></circle>
              <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
          </span>
          <input
            type="text"
            className="search-input"
            placeholder="Search by id, name or description..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
        </div>
      </header>

      {/* Status Notifications */}
      {error && <div className="status-msg error">⚠️ {error}</div>}
      {isLoading && products.length === 0 && <div className="status-msg loading">Syncing with database...</div>}

      {/* Top Grid: Form and Banner */}
      <div className="grid-top">
        {/* Form Card */}
        <section className="card">
          <h2 className="card-title">
            {isEditing ? 'Edit Product' : 'Add Product'}
          </h2>
          <form onSubmit={handleSubmit}>
            <div className="form-grid">
              <div className="form-group">
                <input
                  type="number"
                  name="id"
                  className="form-input"
                  placeholder="ID"
                  value={formData.id}
                  onChange={handleInputChange}
                  disabled={isEditing} // ID should not be modifiable during edits
                  required
                />
              </div>
              <div className="form-group">
                <input
                  type="text"
                  name="name"
                  className="form-input"
                  placeholder="Name"
                  value={formData.name}
                  onChange={handleInputChange}
                  required
                />
              </div>
              <div className="form-group">
                <input
                  type="text"
                  name="description"
                  className="form-input"
                  placeholder="Description"
                  value={formData.description}
                  onChange={handleInputChange}
                  required
                />
              </div>
              <div className="form-group">
                <input
                  type="number"
                  step="0.01"
                  name="price"
                  className="form-input"
                  placeholder="Price"
                  value={formData.price}
                  onChange={handleInputChange}
                  required
                />
              </div>
            </div>

            <div className="form-grid" style={{ marginBottom: '1.5rem' }}>
              <div className="form-group">
                <input
                  type="number"
                  name="quantity"
                  className="form-input"
                  placeholder="Quantity"
                  value={formData.quantity}
                  onChange={handleInputChange}
                  required
                />
              </div>
            </div>

            <div className="form-actions">
              <button type="submit" className="btn-primary">
                {isEditing ? 'Save Changes' : (
                  <>
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" style={{ marginRight: '6px' }}>
                      <line x1="12" y1="5" x2="12" y2="19"></line>
                      <line x1="5" y1="12" x2="19" y2="12"></line>
                    </svg>
                    Add
                  </>
                )}
              </button>
              {isEditing && (
                <button type="button" className="btn-secondary" onClick={handleCancelEdit}>
                  Cancel
                </button>
              )}
            </div>
          </form>
        </section>

        {/* Track Banner Card */}
        <section className="card track-card">
          <div>
            <div className="track-header">
              <span className="track-icon"></span>
              <h2 className="track-title">Track. Manage. Grow.</h2>
            </div>
            <p className="track-desc">
              Streamline your inventory with smart product management that scales with your business.
            </p>
          </div>
          <div className="powered-by">
            Powered By <span className="powered-brand">Telusko</span>
          </div>
        </section>
      </div>

      {/* Bottom Grid: Products Table */}
      <section className="card products-section">
        <h2 className="card-title">Products</h2>
        <div className="products-table-container">
          <table className="products-table">
            <thead>
              <tr>
                <th className="sortable-header" onClick={() => handleSort('id')}>
                  ID
                  <span className="sort-icon">
                    {sortField === 'id' ? (
                      sortOrder === 'asc' ? (
                        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3">
                          <polyline points="18 15 12 9 6 15"></polyline>
                        </svg>
                      ) : (
                        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3">
                          <polyline points="6 9 12 15 18 9"></polyline>
                        </svg>
                      )
                    ) : (
                      <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" opacity="0.3">
                        <polyline points="6 9 12 15 18 9"></polyline>
                      </svg>
                    )}
                  </span>
                </th>
                <th className="sortable-header" onClick={() => handleSort('name')}>
                  Name
                  <span className="sort-icon">
                    {sortField === 'name' ? (
                      sortOrder === 'asc' ? (
                        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3">
                          <polyline points="18 15 12 9 6 15"></polyline>
                        </svg>
                      ) : (
                        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3">
                          <polyline points="6 9 12 15 18 9"></polyline>
                        </svg>
                      )
                    ) : null}
                  </span>
                </th>
                <th>Description</th>
                <th className="sortable-header" onClick={() => handleSort('price')}>
                  Price
                  <span className="sort-icon">
                    {sortField === 'price' ? (
                      sortOrder === 'asc' ? (
                        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3">
                          <polyline points="18 15 12 9 6 15"></polyline>
                        </svg>
                      ) : (
                        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3">
                          <polyline points="6 9 12 15 18 9"></polyline>
                        </svg>
                      )
                    ) : null}
                  </span>
                </th>
                <th className="sortable-header" onClick={() => handleSort('quantity')}>
                  Quantity
                  <span className="sort-icon">
                    {sortField === 'quantity' ? (
                      sortOrder === 'asc' ? (
                        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3">
                          <polyline points="18 15 12 9 6 15"></polyline>
                        </svg>
                      ) : (
                        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3">
                          <polyline points="6 9 12 15 18 9"></polyline>
                        </svg>
                      )
                    ) : null}
                  </span>
                </th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {sortedProducts.length > 0 ? (
                sortedProducts.map((product) => (
                  <tr key={product.id}>
                    <td>{product.id}</td>
                    <td>
                      <div className="product-name">{product.name}</div>
                    </td>
                    <td>
                      <div className="product-desc">{product.description}</div>
                    </td>
                    <td>
                      <div className="product-price">${parseFloat(product.price).toFixed(2)}</div>
                    </td>
                    <td>
                      <span className="quantity-badge">{product.quantity}</span>
                    </td>
                    <td>
                      <div className="action-buttons">
                        <button
                          className="btn-edit"
                          onClick={() => handleEditClick(product)}
                        >
                          Edit
                        </button>
                        <button
                          className="btn-delete"
                          onClick={() => handleDeleteClick(product.id)}
                        >
                          Delete
                        </button>
                      </div>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="6" style={{ textAlign: 'center', padding: '2rem', color: 'var(--text-muted)' }}>
                    {isLoading ? 'Loading products...' : 'No products found'}
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </section>
    </div>
  );
}

export default App;
