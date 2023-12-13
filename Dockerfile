FROM ghcr.io/aylmerbritto/gptchat:base
COPY . .
RUN rm -rf /root/.cache/pip/wheels/
EXPOSE 8050
CMD python3 app.py
