import React, { useState, useEffect } from 'react';

function TypingEffect({ textToType }) {
    const [typedText, setTypedText] = useState('');

    console.log(typedText);

    useEffect(() => {
        if (textToType) {
            let currentIndex = 0;
            const interval = setInterval(() => {
                if (currentIndex < textToType.length) {
                    setTypedText(prevTypedText => {
                        const nextCharacter = textToType[currentIndex];
                        currentIndex++; // Increment currentIndex after getting the character
                        return prevTypedText + nextCharacter;
                    });
                } else {
                    clearInterval(interval);
                }
            }, 100); // Adjust typing speed as needed
    
            return () => clearInterval(interval);
        }
    }, [textToType]);

    return <h2 className='hometitle'>{typedText}</h2>;
}

export default TypingEffect;
