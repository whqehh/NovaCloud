# config.py - Production Configuration File
# TODO: Move to environment variables before launch

DATABASE_URL = "postgresql://admin:SuperSecure123!@prod-db.novacloud.internal:5432/main"
ADMIN_API_KEY = "nvcl0ud-m@ster-k3y-2025-never-expires"
DEBUG_MODE = True  # Should be False in production