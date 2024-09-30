document.addEventListener('DOMContentLoaded', () => {
    // Handle Remove button click
    const removeLinks = document.querySelectorAll('.remove-item');
    removeLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault(); // ป้องกันการลิ้งค์
            const productName = this.getAttribute('data-product');
            if (confirm(`Are you sure you want to remove ${productName} from your cart?`)) {
                window.location.href = this.href; // Redirect เมื่อยืนยันการลบ
            }
        });
    });

    // Handle Checkout button click
    const checkoutBtn = document.getElementById('checkout-btn');
    const checkoutSection = document.getElementById('checkout-section');
    
    checkoutBtn.addEventListener('click', function(event) {
        event.preventDefault(); // ป้องกันการเลื่อนหน้ากระทันหัน

        // Add animation class to the checkout button
        this.classList.add('animate-bounce');

        // Smooth scroll ไปยัง checkout section
        checkoutSection.classList.remove('hidden');
        checkoutSection.scrollIntoView({ behavior: 'smooth' });

        // Remove bounce effect after animation ends
        setTimeout(() => {
            this.classList.remove('animate-bounce');
        }, 1000); // ระยะเวลาเอฟเฟกต์
    });
});

function startOrderProcess() {
    // Hide the form and display the order status
    document.getElementById('checkout-form').style.display = 'none';
    document.getElementById('order-status').style.display = 'block';

    // Animate each step with a delay and bounce effect
    setTimeout(() => {
        let step1 = document.getElementById('status-step-1');
        step1.classList.add('text-orange-500', 'animate-bounce');
        step1.style.transition = "transform 0.5s";
    }, 5000);

    setTimeout(() => {
        let step2 = document.getElementById('status-step-2');
        step2.classList.add('text-orange-500', 'animate-bounce');
        step2.style.transition = "transform 0.5s";
    }, 10000);

    setTimeout(() => {
        let step3 = document.getElementById('status-step-3');
        step3.classList.add('text-orange-500', 'animate-bounce');
        step3.style.transition = "transform 0.5s";
    }, 15000);

    setTimeout(() => {
        let step4 = document.getElementById('status-step-4');
        step4.classList.add('text-orange-500', 'animate-bounce');
        step4.style.transition = "transform 0.5s";
    }, 20000);

    // Submit form after 21 seconds
    setTimeout(() => {
        document.getElementById('checkout-form').submit();
    }, 21000);
}

document.addEventListener('DOMContentLoaded', function() {
    const productName = document.getElementById('product-name').textContent;

    // Add hover animation to buttons
    const buttons = document.querySelectorAll('button, a');
    buttons.forEach(button => {
        button.addEventListener('mouseover', function() {
            button.classList.add('transform', 'scale-105');
        });
        button.addEventListener('mouseout', function() {
            button.classList.remove('transform', 'scale-105');
        });
    });

    // Confirm before form submission
    document.getElementById('delete-form').addEventListener('submit', function(event) {
        const confirmation = confirm(`Are you sure you want to delete "${productName}"? This action cannot be undone.`);
        if (!confirmation) {
            event.preventDefault(); // Prevent form submission if user cancels
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const productName = document.getElementById('product-name').textContent;

    // Confirm before form submission
    document.getElementById('delete-form').addEventListener('submit', function(event) {
        const confirmation = confirm(`Are you sure you want to delete the product "${productName}"? This action cannot be undone.`);
        if (!confirmation) {
            event.preventDefault(); // Prevent form submission if user cancels
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("edit-product-form");
    const submitBtn = document.getElementById("submit-btn");
    const loadingSpinner = document.getElementById("loading-spinner");
  
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      submitBtn.disabled = true;
      submitBtn.classList.add("opacity-50", "cursor-not-allowed");
  
      // Show loading spinner
      loadingSpinner.classList.remove("hidden");
  
      // Simulate form submission delay
      setTimeout(function () {
        form.submit();
      }, 2000); // Simulate delay of 2 seconds
    });
  });

  document.addEventListener("DOMContentLoaded", function() {
    const productCards = document.querySelectorAll(".product-card");

    // Adding a fade-in animation for each product card
    productCards.forEach((card, index) => {
        card.style.opacity = 0;
        card.style.transform = "translateY(50px)";
        setTimeout(() => {
            card.style.transition = "all 0.6s ease-in-out";
            card.style.opacity = 1;
            card.style.transform = "translateY(0)";
        }, index * 200);  // Staggered effect
    });

    // Add hover effect with JS for additional styling
    productCards.forEach(card => {
        card.addEventListener("mouseover", () => {
            card.classList.add("shadow-xl", "transform", "scale-110");
        });
        card.addEventListener("mouseout", () => {
            card.classList.remove("shadow-xl", "transform", "scale-110");
        });
    });
});

document.addEventListener("DOMContentLoaded", () => {
    // Slide in animation for message boxes
    const messages = document.querySelectorAll(".message-box");
    messages.forEach((message, index) => {
        setTimeout(() => {
            message.classList.add("opacity-100");
            message.style.transform = "translateY(0)";
        }, index * 200);  // Staggered animation for each message
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const confirmationContent = document.querySelector(".fade-in");
    confirmationContent.style.opacity = 1;
    confirmationContent.style.transition = "opacity 1s ease-out";
});

document.addEventListener("DOMContentLoaded", () => {
    const content = document.querySelector(".fade-in");
    content.style.opacity = 1;
    content.style.transition = "opacity 1s ease-in-out";
});

document.addEventListener("DOMContentLoaded", () => {
    const content = document.querySelector(".fade-in");
    content.style.opacity = 1;
    content.style.transition = "opacity 1s ease-in-out";
});

document.addEventListener("DOMContentLoaded", () => {
    // Fade-in effect for the main container
    const content = document.querySelector(".fade-in");
    content.style.opacity = 1;
    content.style.transition = "opacity 1s ease-in-out";

    // Fade-in effect for pagination on scroll
    const pagination = document.querySelector(".fade-in-pagination");
    window.addEventListener("scroll", () => {
        if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight) {
            pagination.style.opacity = 1;
            pagination.style.transition = "opacity 1s ease-in-out";
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    // Product image hover zoom effect
    const productImages = document.querySelectorAll('.product-image-zoom');
    
    productImages.forEach(image => {
        image.addEventListener('mouseenter', () => {
            image.style.transform = 'scale(1.1)';
            image.style.transition = 'transform 0.3s ease';
        });
        
        image.addEventListener('mouseleave', () => {
            image.style.transform = 'scale(1)';
        });
    });

    // Smooth scroll to top when clicking the "Back to top" button
    const backToTopButton = document.querySelector('.back-to-top');
    if (backToTopButton) {
        backToTopButton.addEventListener('click', function (e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Fade-in animation for products
    const products = document.querySelectorAll('.product-card');
    
    products.forEach((product, index) => {
        setTimeout(() => {
            product.style.opacity = 1;
            product.style.transform = 'translateY(0)';
            product.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        }, index * 150); // Delay effect for each product
    });
});

document.addEventListener('DOMContentLoaded', function () {
    // Form field focus and blur effects
    const formFields = document.querySelectorAll('input, textarea');
    
    formFields.forEach(field => {
        field.addEventListener('focus', () => {
            field.parentElement.classList.add('focus-within');
        });

        field.addEventListener('blur', () => {
            field.parentElement.classList.remove('focus-within');
        });
    });

    // Button hover effects
    const buttons = document.querySelectorAll('button, a');

    buttons.forEach(button => {
        button.addEventListener('mouseenter', () => {
            button.style.transform = 'scale(1.05)';
            button.style.transition = 'transform 0.3s ease';
        });

        button.addEventListener('mouseleave', () => {
            button.style.transform = 'scale(1)';
        });
    });
    
    // Smooth scrolling for anchor links
    const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');
    
    smoothScrollLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    // Enhance the button hover effect
    const buttons = document.querySelectorAll('button, a');
    
    buttons.forEach(button => {
        button.addEventListener('mouseenter', () => {
            button.style.transform = 'scale(1.05)';
            button.style.transition = 'transform 0.3s ease';
        });

        button.addEventListener('mouseleave', () => {
            button.style.transform = 'scale(1)';
        });
    });
    
    // Smooth scrolling for anchor links
    const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');
    
    smoothScrollLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});



