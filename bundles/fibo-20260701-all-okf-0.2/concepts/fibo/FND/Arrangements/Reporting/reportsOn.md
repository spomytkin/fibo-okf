---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: reports on
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a subject matter, observation(s), assessment(s), focus or other topic of a report
  domain:
  - concept: /concepts/fibo/FND/Arrangements/Reporting/Report.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/Report
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Documents/isAbout
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/reportsOn
sources:
- id: fibo-source-a52060e8b1
  resource: references/fibo/FND/Arrangements/Reporting.rdf
  sha256: a52060e8b187a3f08302027cf7c7be15c9b644d9a3a7105f69a6415913db5143
  title: FIBO source FND/Arrangements/Reporting.rdf
title: reports on
type: Ontology Property
---

# reports on

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Reporting/reportsOn>

## Definition

indicates a subject matter, observation(s), assessment(s), focus or other topic of a report

## Relationships

- **Domain**: [Report](/concepts/fibo/FND/Arrangements/Reporting/Report.md)
- **Subproperty of**: [isAbout](<https://www.omg.org/spec/Commons/Documents/isAbout>)

## Annotations

- **label**: reports on
- **definition**: indicates a subject matter, observation(s), assessment(s), focus or other topic of a report

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
