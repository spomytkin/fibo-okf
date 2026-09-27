---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: state branch of foreign banking organization
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: branch of a foreign bank located in any State of the United States at which deposits are received, established
      and operating under the laws of that State, where state means any State of the United States or the District of Columbia
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.ffiec.gov/npw/Help/InstitutionTypes
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.govinfo.gov/content/pkg/COMPS-275/pdf/COMPS-275.pdf
  disjoint_with:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/FederalBranchOfForeignBankingOrganization.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/FederalBranchOfForeignBankingOrganization
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticBranchOfAForeignBank.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticBranchOfAForeignBank
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/StateBranchOfForeignBankingOrganization
sources:
- id: fibo-source-d9bfee9a32
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
  sha256: d9bfee9a3294cc99a3ff7688e325d68a9cc2158ec209ffd10a9a8e411af37f33
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities.rdf
title: state branch of foreign banking organization
type: Ontology Class
---

# state branch of foreign banking organization

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/StateBranchOfForeignBankingOrganization>

## Definition

branch of a foreign bank located in any State of the United States at which deposits are received, established and operating under the laws of that State, where state means any State of the United States or the District of Columbia

## Relationships

- **Subclass of**: [DomesticBranchOfAForeignBank](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/DomesticBranchOfAForeignBank.md)

## Constraints

- **Disjoint with**: [FederalBranchOfForeignBankingOrganization](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/USFinancialServicesEntities/FederalBranchOfForeignBankingOrganization.md)

## Annotations

- **label**: state branch of foreign banking organization
- **definition**: branch of a foreign bank located in any State of the United States at which deposits are received, established and operating under the laws of that State, where state means any State of the United States or the District of Columbia
- **adaptedFrom**: https://www.ffiec.gov/npw/Help/InstitutionTypes
- **adaptedFrom**: https://www.govinfo.gov/content/pkg/COMPS-275/pdf/COMPS-275.pdf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
