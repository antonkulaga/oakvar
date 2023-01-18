from typing import Optional
from typing import List
from typing import Dict


def run(
    inputs: List[str],
    annotators: List[str] = [],
    annotators_replace: List[str] = [],
    excludes: List[str] = [],
    run_name: List[str] = [],
    output_dir: List[str] = [],
    startat: Optional[str] = None,
    endat: Optional[str] = None,
    skip: List[str] = [],
    confpath: Optional[str] = None,
    conf: dict = {},
    report_types: List[str] = [],
    genome: Optional[str] = None,
    cleandb: bool = False,
    newlog: bool = False,
    note: str = "",
    mp: Optional[int] = None,
    keep_temp: bool = False,
    writeadmindb: bool = False,
    job_name: Optional[List[str]] = None,
    separatesample: bool = False,
    primary_transcript: List[str] = ["mane"],
    clean: bool = False,
    module_options: Dict = {},
    system_option: Dict = {},
    package: Optional[str] = None,
    filtersql: Optional[str] = None,
    includesample: Optional[List[str]] = None,
    excludesample: Optional[List[str]] = None,
    filter: Optional[str] = None,
    filterpath: Optional[str] = None,
    modules_dir: Optional[str] = None,
    preparers: List[str] = [],
    mapper_name: List[str] = [],
    postaggregators: List[str] = [],
    vcf2vcf: bool = False,
    logtofile: bool = False,
    loglevel: str = "INFO",
    combine_input: bool = False,
    input_format: Optional[str] = None,
    input_encoding: Optional[str] = None,
    uid: Optional[str] = None,
    loop=None,
    outer=None,
):
    from ..lib.base.runner import Runner
    from ..lib.util.asyn import get_event_loop

    # nested asyncio
    # nest_asyncio.apply()
    # Custom system conf
    module = Runner(
        inputs=inputs,
        annotators=annotators,
        annotators_replace=annotators_replace,
        excludes=excludes,
        run_name=run_name,
        output_dir=output_dir,
        startat=startat,
        endat=endat,
        skip=skip,
        confpath=confpath,
        conf=conf,
        report_types=report_types,
        genome=genome,
        cleandb=cleandb,
        newlog=newlog,
        note=note,
        mp=mp,
        keep_temp=keep_temp,
        writeadmindb=writeadmindb,
        job_name=job_name,
        separatesample=separatesample,
        primary_transcript=primary_transcript,
        clean=clean,
        module_options=module_options,
        system_option=system_option,
        package=package,
        filtersql=filtersql,
        includesample=includesample,
        excludesample=excludesample,
        filter=filter,
        filterpath=filterpath,
        modules_dir=modules_dir,
        preparers=preparers,
        mapper_name=mapper_name,
        postaggregators=postaggregators,
        vcf2vcf=vcf2vcf,
        logtofile=logtofile,
        loglevel=loglevel,
        combine_input=combine_input,
        input_format=input_format,
        input_encoding=input_encoding,
        uid=uid,
        outer=outer,
    )
    if isinstance(inputs, str):
        inputs = [inputs]
    if isinstance(output_dir, str):
        output_dir = [output_dir]
    if isinstance(run_name, str):
        run_name = [run_name]
    if not loop:
        loop = get_event_loop()
    return loop.run_until_complete(module.main())
