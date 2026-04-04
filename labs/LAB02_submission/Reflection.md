# Lab 2 Reflection

In this lab, both containers ran on your laptop. In production, the preprocessor would run in the warehouse datacenter and the inference API would run in Congo's main datacenter.

**How would the architecture and your `docker run` commands differ if these containers were actually running in separate datacenters?**

Consider:
- How would the preprocessor find the inference API?
- What about the shared volumes?
- What new challenges would arise?


## Your Reflection Below

If we were to move this architecture to containers that were actually located in seperate data centers, we would of course avoid our local host problem. Instead we could point the `API_URL` variable to a real address such as `https://inference.congo-api.com`, I would then need to set up https encription, and a api authentication system so i don't leave our endpoint exposed to the public. Our Shared volume also wouldn't work so we'd likely need to move our storage system for images to something such as a GCP bucket or AWS S3 storage. The data center seperation would obviously introduce latency for each classification request, it would also be harder to monitor if something breaks in your system or an outage occurs. Horizontal scaling of the api could possibly solve this issue, or you could create some sort of "Que" function for each http request.