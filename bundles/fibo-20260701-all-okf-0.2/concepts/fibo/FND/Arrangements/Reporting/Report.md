---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: report
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: document that provides a structured description of something, prepared on ad hoc, periodic, recurring, regular,
      or as required basis
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Reports may refer to specific periods, events, occurrences, or subjects, and may be communicated or presented in
      oral, electronic, or written form.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Documents/hasReportingPeriod
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/hasReportDate
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/DateTime
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/hasReportDateTime
  - filler: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/isReportedTo
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Submitter
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/isSubmittedBy
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/isSubmittedTo
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/ReportingParty
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/isProvidedBy
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Document
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Report
sources:
- id: fibo-source-a52060e8b1
  resource: references/fibo/FND/Arrangements/Reporting.rdf
  sha256: a52060e8b187a3f08302027cf7c7be15c9b644d9a3a7105f69a6415913db5143
  title: FIBO source FND/Arrangements/Reporting.rdf
title: report
type: Ontology Class
---

# report

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Report>

## Definition

document that provides a structured description of something, prepared on ad hoc, periodic, recurring, regular, or as required basis

## Relationships

- **Subclass of**: [Document](<https://www.omg.org/spec/Commons/Documents/Document>)

## Constraints

- **[hasReportingPeriod](/concepts/fibo/FND/Arrangements/Documents/hasReportingPeriod.md)**: min qualified cardinality 0 of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)
- **[hasReportDate](/concepts/fibo/FND/Arrangements/Reporting/hasReportDate.md)**: min qualified cardinality 0 of type [ExplicitDate](<https://www.omg.org/spec/Commons/DatesAndTimes/ExplicitDate>)
- **[hasReportDateTime](/concepts/fibo/FND/Arrangements/Reporting/hasReportDateTime.md)**: min qualified cardinality 0 of type [DateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/DateTime>)
- **[isReportedTo](/concepts/fibo/FND/Arrangements/Reporting/isReportedTo.md)**: some values from of type [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)
- **[isSubmittedBy](/concepts/fibo/FND/Arrangements/Reporting/isSubmittedBy.md)**: min qualified cardinality 0 of type [Submitter](/concepts/fibo/FND/Arrangements/Reporting/Submitter.md)
- **[isSubmittedTo](/concepts/fibo/FND/Arrangements/Reporting/isSubmittedTo.md)**: min qualified cardinality 0 of type [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)
- **[isProvidedBy](<https://www.omg.org/spec/Commons/Organizations/isProvidedBy>)**: some values from of type [ReportingParty](/concepts/fibo/FND/Arrangements/Reporting/ReportingParty.md)

## Annotations

- **label**: report
- **definition**: document that provides a structured description of something, prepared on ad hoc, periodic, recurring, regular, or as required basis
- **explanatoryNote**: Reports may refer to specific periods, events, occurrences, or subjects, and may be communicated or presented in oral, electronic, or written form.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
