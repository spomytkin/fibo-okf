---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: non-depository institution
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial institution that does not have a full banking license and typically is not supervised by a national or
      international banking regulatory agency
  - predicate: http://www.w3.org/2004/02/skos/core#historyNote
    value: The term 'non-bank' may have been derived from 'non-deposit taking banking institution'. To be clearer, in the
      United States, non-depository institutions are explicitly disjoint with depository institutions (financial institutions
      that take deposits of some sort, potentially including securities) in FIBO. Banks are defined as financial institutions
      that take demand deposits from the public and that also provide commercial lending services. Many 'non-bank' institutions
      take deposits or provide commercial lending services, but they may not do both.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Banking Terms, Sixth Edition, 2012
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.worldbank.org/en/publication/gfdr/gfdr-2016/background/nonbank-financial-institution
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A non-depository financial institution acts as a middleman between two parties in a financial transaction, and
      does not provide traditional depository services, such as brokerage firms, insurance companies, and investment companies.
      These kinds of institutions facilitate alternative financial services, such as investment (both collective and individual),
      risk pooling, financial consulting, brokering, money transmission, and check cashing. NBFIs are a source of consumer
      credit (along with licensed banks). Examples of nonbank financial institutions include insurance firms, venture capitalists,
      currency exchanges, some microloan organizations, and pawn shops. These non-bank financial institutions provide services
      that are not necessarily suited to banks, serve as competition to banks, and specialize in sectors or groups. Note,
      however, that there are exceptions in Europe, for example, where the same firm may have banking, insurance, and brokerage
      functions.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: non-bank financial company (NBFC)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: non-bank financial institution (NBFI)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: non-banking financial institution (NBFI)
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: non-depository institution
type: Ontology Class
---

# non-depository institution

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/NonDepositoryInstitution>

## Definition

financial institution that does not have a full banking license and typically is not supervised by a national or international banking regulatory agency

## Relationships

- **Subclass of**: [FinancialInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)

## Annotations

- **label**: non-depository institution
- **definition**: financial institution that does not have a full banking license and typically is not supervised by a national or international banking regulatory agency
- **historyNote**: The term 'non-bank' may have been derived from 'non-deposit taking banking institution'. To be clearer, in the United States, non-depository institutions are explicitly disjoint with depository institutions (financial institutions that take deposits of some sort, potentially including securities) in FIBO. Banks are defined as financial institutions that take demand deposits from the public and that also provide commercial lending services. Many 'non-bank' institutions take deposits or provide commercial lending services, but they may not do both.
- **adaptedFrom**: Barron's Dictionary of Banking Terms, Sixth Edition, 2012
- **adaptedFrom**: https://www.worldbank.org/en/publication/gfdr/gfdr-2016/background/nonbank-financial-institution
- **explanatoryNote**: A non-depository financial institution acts as a middleman between two parties in a financial transaction, and does not provide traditional depository services, such as brokerage firms, insurance companies, and investment companies. These kinds of institutions facilitate alternative financial services, such as investment (both collective and individual), risk pooling, financial consulting, brokering, money transmission, and check cashing. NBFIs are a source of consumer credit (along with licensed banks). Examples of nonbank financial institutions include insurance firms, venture capitalists, currency exchanges, some microloan organizations, and pawn shops. These non-bank financial institutions provide services that are not necessarily suited to banks, serve as competition to banks, and specialize in sectors or groups. Note, however, that there are exceptions in Europe, for example, where the same firm may have banking, insurance, and brokerage functions.
- **synonym**: non-bank financial company (NBFC)
- **synonym**: non-bank financial institution (NBFI)
- **synonym**: non-banking financial institution (NBFI)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
