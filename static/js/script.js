document.addEventListener('DOMContentLoaded', function() {
    // Obtendo elementos do DOM
    const searchInput = document.getElementById('search-input');
    const priceFilter = document.getElementById('price-filter');
    const books = document.querySelectorAll('.book');
    const paginationButtons = document.querySelectorAll('.pagination button');
    const itemsPerPage = 24;
    let currentPage = 1;

    // Inicializar a paginação
    function initializePagination() {
        currentPage = 1;
        updatePaginationButtons();
        showBooks();
    }

    initializePagination();

    // Mostrar os livros na página atual
    function showBooks() {
        const startIdx = (currentPage - 1) * itemsPerPage;
        const endIdx = startIdx + itemsPerPage;

        books.forEach(function(book, index) {
            if (index >= startIdx && index < endIdx) {
                book.style.display = 'block';
            } else {
                book.style.display = 'none';
            }
        });
    }

    // Atualizar os botões de paginação
    function updatePaginationButtons() {
        if (currentPage === 1) {
            document.querySelector('.previous-page').disabled = true;
        } else {
            document.querySelector('.previous-page').disabled = false;
        }

        if (currentPage * itemsPerPage >= books.length) {
            document.querySelector('.next-page').disabled = true;
        } else {
            document.querySelector('.next-page').disabled = false;
        }
    }

    // Filtrar os livros
    function filterBooks() {
        const priceFilterValue = priceFilter.value;
        const sortedBooks = [...books].sort((a, b) => {
            const priceA = parseFloat(a.querySelector('.book-real-price').textContent.replace('R$', '').trim());
            const priceB = parseFloat(b.querySelector('.book-real-price').textContent.replace('R$', '').trim());
            
            if (priceFilterValue === 'cheap') {
                return priceA - priceB; 
            } else if (priceFilterValue === 'expensive') {
                return priceB - priceA; 
            } else {
                const titleA = a.querySelector('.book-title').textContent.toLowerCase();
                const titleB = b.querySelector('.book-title').textContent.toLowerCase();
                return titleA.localeCompare(titleB);
            }
        });
        
        const bookList = document.querySelector('.book-list');
        bookList.innerHTML = ''; 
        
        sortedBooks.forEach(book => bookList.appendChild(book));
        currentPage = 1;
        updatePaginationButtons();
        showBooks();
    }

    // Filtrar os livros por título
    function filterBooksByTitle() {
        const searchFilter = searchInput.value.toLowerCase();
        books.forEach(function(book) {
            const title = book.querySelector('.book-title').textContent.toLowerCase();
            if (title.includes(searchFilter)) {
                book.style.display = 'block';
            } else {
                book.style.display = 'none';
            }
        });
    
        updatePaginationButtons();
    }

    // Adicione este código após o evento 'DOMContentLoaded'
    document.getElementById('search-icon').addEventListener('click', function() {
        filterBooksByTitle();
    });

    // Adicionando event listener para input no campo de busca
    searchInput.addEventListener('input', function() {
        filterBooksByTitle();
    });

    // Adicionando event listener para seleção no filtro de preço
    priceFilter.addEventListener('change', function() {
        currentPage = 1;
        filterBooks();
    });

    // Adicionando event listener para os botões de paginação
    paginationButtons.forEach(button => {
        button.addEventListener('click', function() {
            if (this.classList.contains('previous-page') && currentPage > 1) {
                currentPage--;
            } else if (this.classList.contains('next-page') && currentPage * itemsPerPage < books.length) {
                currentPage++;
            }

            if (currentPage < 1) {
                currentPage = 1;
            }

            updatePaginationButtons();
            showBooks();
        });
    });
});