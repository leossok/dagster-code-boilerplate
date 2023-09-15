# build stage
FROM python:3.9 AS builder

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# copy files
COPY . /project/

# install dependencies and project into the local packages directory
WORKDIR /project
RUN mkdir __pypackages__ && pdm sync --prod --no-editable


# run stage
FROM python:3.9

# retrieve packages from build stage
ENV PYTHONPATH=/project/pkgs
COPY --from=builder /project/__pypackages__/3.9/lib /project/pkgs

# retrieve executables
COPY --from=builder /project/__pypackages__/3.9/bin/* /bin/

COPY --from=builder /project /user_code/src

# Post-installation (if needed)
# RUN playwright install
# RUN playwright install-deps

# set command/entrypoint, adapt to fit your needs
CMD ["dagster", "code-server", "start", "-h", "0.0.0.0", "-p", "4000", "-m", "data_pipeline"]