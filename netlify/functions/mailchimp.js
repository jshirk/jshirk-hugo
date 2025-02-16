const fetch = require("node-fetch");

exports.handler = async (event) => {
    const { email, fname } = JSON.parse(event.body);
    
    if (!email || !fname) {
        return {
            statusCode: 400,
            body: JSON.stringify({ error: "Missing email or name" }),
        };
    }

    const url = "https://jshirk.us2.list-manage.com/subscribe/post?u=494bbc345ee9ac49815fc27f7&id=96f30fa52e";
    const params = new URLSearchParams();
    params.append("EMAIL", email);
    params.append("FNAME", fname);

    try {
        const response = await fetch(url, {
            method: "POST",
            body: params,
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
        });

        return {
            statusCode: 200,
            body: JSON.stringify({ message: "Subscribed successfully!" }),
        };
    } catch (error) {
        return {
            statusCode: 500,
            body: JSON.stringify({ error: "Failed to subscribe" }),
        };
    }
};