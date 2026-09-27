---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: savings association
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: depository institution that is (a) any federal savings bank or association chartered under section 1464 of the
      Federal Deposit Insurance Act; (b) any state chartered building and loan association, savings and loan association,
      or homestead association; or (c) any cooperative bank (other than a cooperative bank which is a state bank as defined
      in subsection (a)(2)) of the Federal Deposit Insurance Act, which is organized and operating according to the laws of
      the State (as defined in subsection (a)(3)) in which it is chartered or organized; and (c) any corporation (other than
      a bank) that the board of directors and the comptroller of the currency jointly determine to be operating in substantially
      the same manner as such a depository institution
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.fdic.gov/regulations/laws/rules/1000-400.html#fdic1000sec.3a
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/SavingsAssociation
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: savings association
type: Ontology Class
---

# savings association

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/SavingsAssociation>

## Definition

depository institution that is (a) any federal savings bank or association chartered under section 1464 of the Federal Deposit Insurance Act; (b) any state chartered building and loan association, savings and loan association, or homestead association; or (c) any cooperative bank (other than a cooperative bank which is a state bank as defined in subsection (a)(2)) of the Federal Deposit Insurance Act, which is organized and operating according to the laws of the State (as defined in subsection (a)(3)) in which it is chartered or organized; and (c) any corporation (other than a bank) that the board of directors and the comptroller of the currency jointly determine to be operating in substantially the same manner as such a depository institution

## Relationships

- **Subclass of**: [DepositoryInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/DepositoryInstitution.md)

## Annotations

- **label**: savings association
- **definition**: depository institution that is (a) any federal savings bank or association chartered under section 1464 of the Federal Deposit Insurance Act; (b) any state chartered building and loan association, savings and loan association, or homestead association; or (c) any cooperative bank (other than a cooperative bank which is a state bank as defined in subsection (a)(2)) of the Federal Deposit Insurance Act, which is organized and operating according to the laws of the State (as defined in subsection (a)(3)) in which it is chartered or organized; and (c) any corporation (other than a bank) that the board of directors and the comptroller of the currency jointly determine to be operating in substantially the same manner as such a depository institution
- **adaptedFrom**: https://www.fdic.gov/regulations/laws/rules/1000-400.html#fdic1000sec.3a

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
