import express from "express";

// Security
import rateLimit from "express-rate-limit";
import helmet from "helmet";
import cors from "cors";
import * as dotenv from "dotenv"; // see https://github.com/motdotla/dotenv#how-do-i-use-dotenv-with-import
dotenv.config();

const app = express();

app.use(helmet());

app.use(express.json());
app.use(express.static("public"));

const limiter = rateLimit({
	windowMs: 5 * 60 * 1000, // 15 minutes
	max: 100, // Limit each IP to 100 requests per `window` (here, per 15 minutes)
	standardHeaders: true, // Return rate limit info in the `RateLimit-*` headers
	legacyHeaders: false, // Disable the `X-RateLimit-*` headers
});

// Apply the rate limiting middleware to all requests
app.use(limiter);

app.use(
	cors({
		origin: true,
		optionsSuccessStatus: 200,
		credentials: true,
	})
);

// health route
app.get("/", (req, res) => {
	return res.status(200).json({
		message: "online",
	});
});

const port = process.env.PORT || 3000;

app.listen(port, () =>
	console.log(`
🚀 Server ready at: http://localhost:${port}
`)
);
