// Create a new component called BookList that uses axios to fetch the list of books from the Flask backend and render them

import React, { useState, useEffect} from 'react';
import axios from 'axios';

function BookList() {
    const [books, setBooks] = useState([]);

    useEffect(() => {
        axios.get('/api/books')
        .then(response => {
            setBooks(response.data);
        })
        .catch(error => {
            console.log(error);
        });
    }, []);

    return(
        <div>
            <h2>Books</h2>
            <ul>
                {books.map(book => (
                    <li key={book.id}>{book.title} by {book.author}</li>
                ))}
            </ul>
        </div>
    );
}

export default BookList;

