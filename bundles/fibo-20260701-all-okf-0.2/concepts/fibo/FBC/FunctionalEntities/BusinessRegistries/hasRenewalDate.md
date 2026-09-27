---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has renewal date
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the date by which a specific registration in the registry must be renewed or updated
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.swift.com/standards/data-standards/bic?tl=en#BICPolicyandDatarecord
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: This property is equivalent to the date of expiry in some registries, such as the BIC registry.
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/RegistrationAuthorities/hasRegistrationDate
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRenewalDate
sources:
- id: fibo-source-fdadb56cd3
  resource: references/fibo/FBC/FunctionalEntities/BusinessRegistries.rdf
  sha256: fdadb56cd346c7f354007b53bb21e21e35b8d83160f45c626d0f675b7b14754d
  title: FIBO source FBC/FunctionalEntities/BusinessRegistries.rdf
title: has renewal date
type: Ontology Property
---

# has renewal date

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRenewalDate>

## Definition

indicates the date by which a specific registration in the registry must be renewed or updated

## Relationships

- **Range**: [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)
- **Subproperty of**: [hasRegistrationDate](<https://www.omg.org/spec/Commons/RegistrationAuthorities/hasRegistrationDate>)

## Annotations

- **label**: has renewal date
- **definition**: indicates the date by which a specific registration in the registry must be renewed or updated
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
- **adaptedFrom**: https://www.swift.com/standards/data-standards/bic?tl=en#BICPolicyandDatarecord
- **usageNote**: This property is equivalent to the date of expiry in some registries, such as the BIC registry.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
