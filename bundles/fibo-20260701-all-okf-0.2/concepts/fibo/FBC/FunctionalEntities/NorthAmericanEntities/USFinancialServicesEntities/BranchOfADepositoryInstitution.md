---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: branch of a depository institution
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: any office or any place of business located in any State of the United States at which deposits are received
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-211/subpart-B/section-211.21
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/isPartOf
    value: Nfbad3dec2b1247588e8905d7ef66b4c3
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/Branch.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/FormalBusinessOrganizations/Branch
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/BranchOfADepositoryInstitution
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
title: branch of a depository institution
type: Ontology Class
---

# branch of a depository institution

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/BranchOfADepositoryInstitution>

## Definition

any office or any place of business located in any State of the United States at which deposits are received

## Relationships

- **Subclass of**: [Branch](/concepts/fibo/BE/LegalEntities/FormalBusinessOrganizations/Branch.md)

## Constraints

- **[isPartOf](<https://www.omg.org/spec/Commons/Collections/isPartOf>)**: some values from value `Nfbad3dec2b1247588e8905d7ef66b4c3`

## Annotations

- **label**: branch of a depository institution
- **definition**: any office or any place of business located in any State of the United States at which deposits are received
- **adaptedFrom**: https://www.ecfr.gov/current/title-12/chapter-II/subchapter-A/part-211/subpart-B/section-211.21

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
